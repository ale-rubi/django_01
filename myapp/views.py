from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.
def index (request):
    return HttpResponse("Index Page")

def hello(request,username):
    print(username)
    return HttpResponse("<h1>Hello World %s</h1>" % username)

def about(request):
    return HttpResponse("About")

def project(request):
    project = list(Project.objects.values())
    return JsonResponse (project, safe=False)

def task(request, id):
    task = get_object_or_404(Task, id=id)
    return HttpResponse('task: %s' % task.title)