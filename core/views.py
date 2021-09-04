from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html', {})


def task(request):
    return render(request, 'task.html', {"title_pager": "Create scheduled task with cronjob, celery and async in python", "author": "by Steve Nguyen"})