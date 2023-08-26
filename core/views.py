from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html', {})


def task(request):
    return render(request, 'task.html', {"title_pager": "Create scheduled tasks with cronjob, celery and async in python", "author": "by Steve Nguyen"})

def paypal(request):
    return render(request, 'paypal.html', {"title_pager": "PayPal Payment Integration Guide In Service API", "author": "by Steve Nguyen"})

def in_app(request):
    return render(request, 'in_app.html', {"title_pager": "In-App Payment Guide In Service API", "author": "by Steve Nguyen"})

def oauth(request):
    return render(request, 'oauth.html', {"title_pager": "OAuth And OAuth2 Workflow", "author": "by Steve Nguyen"})

def minio(request):
    return render(request, 'minio.html', {"title_pager": "Amazon S3 And Minio Object Storage Service", "author": "by Steve Nguyen"})

def unit_test(request):
    return render(request, 'unit_test.html', {"title_pager": "Unit Test And Selenium Guide", "author": "by Steve Nguyen"})

def pythonanywhere(request):
    return render(request, 'pythonanywhere.html', {"title_pager": "Deploy Django on Pythonanywhere Guide", "author": "by Steve Nguyen"})


def reactnativewithexpo(request):
    return render(request, 'reactnativewithexpo.html', {"title_pager": "Build React Native application using Expo", "author": "by Steve Nguyen"})