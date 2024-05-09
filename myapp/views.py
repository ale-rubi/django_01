from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject

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
    return render(request,'projects/project.html',{
        'project':project
    })

def task(request):
    #task = Task.objects.get(title=title)
    task = Task.objects.all()
    return render(request,'tasks/task.html',{
        'task':task
    })

def create_task(request):
    if request.method == 'GET':
        # show interface
         return render(request,'tasks/create_task.html',{
        'form': CreateNewTask()
    })
    else:
        Task.objects.create(title=request.POST['title'],description=request.POST['description'],project_id=1)
        return redirect('/task/')
    
def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html',{
            'form':CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST["name"])
        return redirect('/project/')
 