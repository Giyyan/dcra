from django.views.generic import TemplateView
from djcelery.models import TaskState
from dcra.celery import app as celery_app


class TasksView(TemplateView):
    template_name = 'tasks.html'

    def get_context_data(self, **kwargs):
        context = super(TasksView, self).get_context_data(**kwargs)
        context['tasks'] = TaskState.objects.all()
        return context