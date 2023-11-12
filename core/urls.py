from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create-scheduled-tasks-with-cronjob-celery-and-async-in-python.html', views.task, name='task'),
    path('paypal-payments-integration-guide.html', views.paypal, name='paypal'),
    path('in-app-payments-integration-guide.html', views.in_app, name='in_app'),
    path('oauth-and-oauth2-workflow.html', views.oauth, name='oauth'),
    path('amazon-s3-and-minio-object-storage-service.html', views.minio, name='minio'),
    path('unit-test-selenium-guide.html', views.unit_test, name='unit-test'),
    path('deploy-django-on-pythonanywhere.html', views.pythonanywhere, name='pythonanywhere'),
    path('react-native-with-expo.html', views.reactnativewithexpo, name='reactnativewithexpo'),
    path('publish-app-android-google-store.html', views.publishappandroidgooglestore, name='publishappandroidgooglestore'),
    path('debug-in-api-management-azure.html', views.apimanagement, name='apimanagement'),
    path('app-service-azure.html', views.appservice, name='appservice'),
    path('publish-application-app-store.html', views.appstore, name='appstore'),
    path('function-app-azure.html', views.function, name='function'),
    path('lambda-function-aws.html', views.lambda_function, name='lambda_function'),
    path('install-boto3-layer-in-aws.html', views.boto3, name='boto3'),
    path('promise-js.html', views.promise, name='promise'),
    path('migration-django.html', views.migration, name='migration'),
    path('compare-packages-javascript.html', views.concept, name='concept'),
    path('junie', views.junie, name='junie'),
]