from celery import states
from djcelery.models import TaskState
from tastypie.resources import ModelResource

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