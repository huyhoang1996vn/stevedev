from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    blogs = [
        {"image": "expo.jpeg", "title": "Build React Native application using Expo", "desc":"Developers don't need macOS to build mobile app.", "url": "reactnativewithexpo"},
        {"image": "publish.jpeg", "title": "Publish android application to Google", "desc":"Publishment application to Google play often require many process.", "url": "publishappandroidgooglestore"},
        {"image": "appstore.jpeg", "title": "Publish application to App Store", "desc":"IOS application is indispensable part of mobile project.", "url": "appstore"},
        {"image": "management.png", "title": "Debug in API Management Azure", "desc":"How to trace requests in api gateway management.", "url": "apimanagement"},
        {"image": "appservice.png", "title": "Azure App Service Guide", "desc":"Cloud service helps developers so munch in deployment.", "url": "appservice"},
        {"image": "function.png", "title": "Function app serverless on Azure", "desc":"Traditionally, we choose plaftform, set up version language, install libraries..", "url": "function"},
        {"image": "azure-devops.png", "title": "CI/CD in Azure Devops", "desc":"Building a Continuous Integration Pipeline in Azure DevOps.", "url": "devops"},
        {"image": "aws-lambda.webp", "title": "AWS Lambda function", "desc":"Lambda function is the most popular technique every developers all know.", "url": "lambda_function"},
        {"image": "layer2.jpeg", "title": "Install Boto3 in layer AWS Lambda function", "desc":"Lambda function is the most popular technique every developers all know.", "url": "boto3"},
        {"image": "minio.jpeg", "title": "Minio Object Storage Service (like Amazon S3)", "desc":"Object storage service is more popular for several reasons.", "url": "minio"},
        {"image": "ai-panel.png", "title": "Neural network Foundamental", "desc":"Artificial Intelligence Foundamental for beginners.", "url": "ai"},
        {"image": "migrations.jpeg", "title": "Migrations in django", "desc":"Migrations are Django’s way of applying changes you make to your models.", "url": "migration"},
        {"image": "any.png", "title": "Deploy Django on Pythonanywhere Guide", "desc":"Deployment is required process in software.", "url": "pythonanywhere"},
        {"image": "test.png", "title": "Unit Test And Selenium in python", "desc":"Testing is a necessary part of the development process but not all.", "url": "unit-test"},
        {"image": "promise.png", "title": "Promise Vs Async/Await in javascript", "desc":"How difference between Promise chains and Async/Await.", "url": "promise"},
        {"image": "npm.jpeg", "title": "Compare packages in javascript", "desc":"Explain and compare popular concept like npm, yarn and so on.", "url": "concept"},
        {"image": "cronjob.png", "title": "Cronjob, Celery and Scheduled tasks in python", "desc":"Cronjob is a solution I got exposed to at first.", "url": "task"},
        {"image": "oath2.png", "title": "OAuth And OAuth2 Workflow", "desc":"OAuth (Open Authorization) is an open standard for authentication and authorization.", "url": "oauth"},
        {"image": "paypal.png", "title": "PayPal Payment Integration Guide In Service API", "desc":"They are webhook paypal and api payment paypal.", "url": "paypal"},
        {"image": "in-app.jpeg", "title": "In-App Payment Guide In Service API", "desc":"In-App payment is available and supported by Apple and Google.", "url": "in_app"},
        {"image": "collation.png", "title": "Collation in SQL", "desc":"Rule for store and query data in sql.", "url": "collation"}
    ]
    return render(request, 'index.html', {"blogs": blogs})


def task(request):
    return render(request, 'task.html', {"title_pager": "Create scheduled tasks with cronjob, celery and async in python", "author": "by Steve Nguyen"})

def paypal(request):
    return render(request, 'paypal.html', {"title_pager": "PayPal Payment Integration Guide In Service API", "author": "by Steve Nguyen"})

def in_app(request):
    return render(request, 'in_app.html', {"title_pager": "In-App Payment Guide In Service API", "author": "by Steve Nguyen"})

def oauth(request):
    return render(request, 'oauth.html', {"title_pager": "OAuth And OAuth2 Workflow", "author": "by Steve Nguyen"})

def minio(request):
    return render(request, 'minio.html', {"title_pager": "Minio Object Storage Service (like Amazon S3)", "author": "by Steve Nguyen"})

def unit_test(request):
    return render(request, 'unit_test.html', {"title_pager": "Unit Test And Selenium Guide", "author": "by Steve Nguyen"})

def pythonanywhere(request):
    return render(request, 'pythonanywhere.html', {"title_pager": "Deploy Django on Pythonanywhere Guide", "author": "by Steve Nguyen"})


def reactnativewithexpo(request):
    return render(request, 'reactnativewithexpo.html', {"title_pager": "Build React Native application using Expo", "author": "by Steve Nguyen"})

def publishappandroidgooglestore(request):
    return render(request, 'android.html', {"title_pager": "Publish application on Google play store", "author": "by Steve Nguyen"})    

def apimanagement(request):
    return render(request, 'apimanagement.html', {"title_pager": "Debug in API Management Azure", "author": "by Steve Nguyen"})   

def appservice(request):
    return render(request, 'appservice.html', {"title_pager": "Explore Azure App Service", "author": "by Steve Nguyen"})       

def appstore(request):
    return render(request, 'appstore.html', {"title_pager": "Publish application on AppStore", "author": "by Steve Nguyen"})    

def function(request):
    return render(request, 'function.html', {"title_pager": "Function app serverless on Azure", "author": "by Steve Nguyen"})             

def lambda_function(request):
    return render(request, 'lambda_function.html', {"title_pager": "Lambda function AWS", "author": "by Steve Nguyen"})          

def boto3(request):
    return render(request, 'boto3.html', {"title_pager": "Install Boto3 in layer AWS lambda function", "author": "by Steve Nguyen"})              

def promise(request):
    return render(request, 'promise.html', {"title_pager": "Promise Vs Async/Await in javascript", "author": "by Steve Nguyen"})        

def migration(request):
    return render(request, 'migrations.html', {"title_pager": "Migrations in django", "author": "by Steve Nguyen"})        

def concept(request):
    return render(request, 'npm.html', {"title_pager": "Compare packages in javascript", "author": "by Steve Nguyen"})        

def devops(request):
    return render(request, 'devops.html', {"title_pager": "CI/CD in Azure Devops", "author": "by Steve Nguyen"})        

def ai(request):
    return render(request, 'ai.html', {"title_pager": "Neural Network Foundamental", "author": "by Steve Nguyen"})        

def collations(request):
    return render(request, 'collations.html', {"title_pager": "SQL Collation", "author": "by Steve Nguyen"})        

