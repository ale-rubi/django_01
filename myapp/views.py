from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render

# Create your views here.
def index (request):
    title = 'Welcome to Django App'
    return render(request,'index.html', {
        'title':title
    })

def about(request):
    username = 'Ale'
    return render(request,'about.html', {
        'username':username
    })

def project(request):
    #project = list(Project.objects.values())
    project = Project.objects.all()
    return render(request,'project.html',{
        'project':project
    })

def task(request):
    #task = Task.objects.get(title=title)
    task = Task.objects.all()
    return render(request,'task.html',{
        'task':task
    })
 