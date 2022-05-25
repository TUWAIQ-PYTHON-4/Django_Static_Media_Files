from django.shortcuts import render
from .models import Task, Project

# Create your views here.

def project_object(request):
    project_objects = Project.objects.all()

    context = {'project':project_objects}

    return render(request, 'project.html', context)


def project_tasks_object(request):
    tasks_objects = Task.objects.all()

    context = {'task':tasks_objects}

    return render(request, 'tasks.html', context)




