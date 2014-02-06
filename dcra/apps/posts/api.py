from celery import states
from djcelery.models import TaskState
from tastypie import fields
from tastypie.resources import ModelResource, Resource
from dcra.celery import app as celery_app
from celery.events.state import Task

TASK_STATE_COLORS = {
    states.SUCCESS: 'label-success',
    states.FAILURE: 'label-danger',
    states.REVOKED: 'label-default',
    states.STARTED: 'label-info',
    states.RETRY: 'label-warning',
    'RECEIVED': 'label-primary'
}


class TaskResource(ModelResource):
    class Meta:
        queryset = TaskState.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'task'

    def dehydrate(self, bundle):
        bundle.data['label'] = TASK_STATE_COLORS[bundle.obj.state]
        return bundle


class TaskObject(object):
    def __init__(self, initial=None):
        self.__dict__['_data'] = {}

        if hasattr(initial, 'items'):
            self.__dict__['_data'] = initial

    def __getattr__(self, name):
        return self._data.get(name, None)

    def __setattr__(self, name, value):
        self.__dict__['_data'][name] = value

    def to_dict(self):
        return self._data

# u'delivery_info':
# {
#                       u'priority': None,
#                       u'redelivered': False,
#                       u'routing_key': u'celery',
#                       u'exchange': u'celery'
#                   },


class TasksResource(Resource):
    args = fields.CharField(attribute='args')
    time_start = fields.FloatField(attribute='time_start')
    name = fields.CharField(attribute='name')
    hostname = fields.CharField(attribute='hostname')
    acknowledged = fields.BooleanField(attribute='acknowledged')
    kwargs = fields.CharField(attribute='kwargs')
    task_id = fields.CharField(attribute='task_id')
    worker_pid = fields.IntegerField(attribute='worker_pid')
    state = fields.CharField(attribute='status')

    class Meta:
        resource_name = 'riak'
        object_class = TaskObject

    def get_object_list(self, request):
        inspect = celery_app.control.inspect()
        inspect.active()

        results = []

        for result_list in inspect.active().values():
            for result in result_list:
                new_obj = TaskObject()
                new_obj.args = result['args']
                new_obj.time_start = result['time_start']
                new_obj.name = result['name']
                new_obj.hostname = result['hostname']
                new_obj.acknowledged = result['acknowledged']
                new_obj.kwargs = result['kwargs']
                new_obj.task_id = result['id']
                new_obj.worker_pid = result['worker_pid']
                new_obj.status = Task(result['id']).state
                results.append(new_obj)

        return results

    def obj_get_list(self, bundle, **kwargs):
        # Filtering disabled for brevity...
        return self.get_object_list(bundle.request)
