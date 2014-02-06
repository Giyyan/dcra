from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from dcra.apps.posts.api import TaskResource
from dcra.apps.posts.views import TasksView

admin.autodiscover()

task_resource = TaskResource()

urlpatterns = patterns(
    '',
    # url(r'^$', TemplateView.as_view(template_name='tasks.html')),
    url(r'^$', TasksView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(task_resource.urls)),
)
