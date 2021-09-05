from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create-scheduled-tasks-with-cronjob-celery-and-async-in-python.html', views.task, name='task'),
]