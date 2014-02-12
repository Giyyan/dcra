import logging
from pprint import pformat
from celery.events import EventReceiver
from django.views.generic import TemplateView
from djcelery.models import TaskState
from dcra.celery import app as celery_app
from celery.events.state import Worker, Task
from celery.result import AsyncResult, GroupResult, allow_join_result
from celery.events.state import State


class TasksView(TemplateView):
    template_name = 'tasks.html'

    def get_context_data(self, **kwargs):
        context = super(TasksView, self).get_context_data(**kwargs)
        # i = celery_app.control.inspect(timeout=2)
        # print('Inspecting workers...')
        # stats = i.stats()
        # print('Stats: %s' % pformat(stats))
        # registered = i.registered()
        # print('Registered: %s' % pformat(registered))
        # scheduled = i.scheduled()
        # print('Scheduled: %s' % pformat(scheduled))
        # active = i.active()
        # print('Active: %s' % pformat(active))
        # reserved = i.reserved()
        # print('Reserved: %s' % pformat(reserved))
        # revoked = i.revoked()
        # print('Revoked: %s' % pformat(revoked))
        # ping = i.ping()
        # print('Ping: %s' % pformat(ping))
        # active_queues = i.active_queues()
        # print('Active queues: %s' % pformat(active_queues))
        
        print(celery_app.Worker.info)
        state = State(workers=celery_app.Worker)
        print(AsyncResult("c833373c-2e5d-4706-84e6-637a19bf1e68"))
        print(AsyncResult("212610b024a24b31a216d8a27b768153").state)
        print([task for task in state.tasks_by_timestamp(limit=1000)])
        # context['tasks'] = TaskState.objects.all()
        return context