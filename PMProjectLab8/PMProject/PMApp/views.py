from django.shortcuts import render
from .models import Project, Task
from . import models


def base(request):

    return render(request, "base.html")


def project(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, "project.html",context)


def task(request):
    context = Task.objects.all()
    return render(request, "task.html", {'context': context})
