import logging
from pprint import pformat
from django.views.generic import TemplateView
from djcelery.models import TaskState
from dcra.celery import app as celery_app
from celery.events.state import Worker, Task


class TasksView(TemplateView):
    template_name = 'tasks.html'

    def get_context_data(self, **kwargs):
        context = super(TasksView, self).get_context_data(**kwargs)
        i = celery_app.control.inspect(timeout=2)
        print('Inspecting workers...')
        stats = i.stats()
        print('Stats: %s' % pformat(stats))
        registered = i.registered()
        print('Registered: %s' % pformat(registered))
        scheduled = i.scheduled()
        print('Scheduled: %s' % pformat(scheduled))
        active = i.active()
        print('Active: %s' % pformat(active))
        reserved = i.reserved()
        print('Reserved: %s' % pformat(reserved))
        revoked = i.revoked()
        print('Revoked: %s' % pformat(revoked))
        ping = i.ping()
        print('Ping: %s' % pformat(ping))
        active_queues = i.active_queues()
        print('Active queues: %s' % pformat(active_queues))

        # worker = celery_app.Worker()
        # state = celery_app.events.state
        # print(state)
        # print(celery_app.WorkController.stats)
        # for _, task in state.itertasks():
        #     print(task)
        # w = Worker(worker)
        # print(worker.active)
        # context['tasks'] = TaskState.objects.all()
        return context