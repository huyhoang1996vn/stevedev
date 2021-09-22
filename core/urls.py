from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create-scheduled-tasks-with-cronjob-celery-and-async-in-python.html', views.task, name='task'),
    path('paypal-payments-integration-guide.html', views.paypal, name='paypal'),
    path('in-app-payments-integration-guide.html', views.in_app, name='in_app'),
    path('oauth-and-oauth2-workflow.html', views.oauth, name='oauth'),
    path('amazon-s3-and-minio-object-storage-service.html', views.minio, name='minio'),
]