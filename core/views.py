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
