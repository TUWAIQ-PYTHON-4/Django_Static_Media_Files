from django.shortcuts import render
from PMApp.models import Task, Project


def project(request):
    proj= Project.objects.all()
    project=[]
    for P in proj:
        project.append({'P':P})
    context ={'project': project}
    return render(request, "base.html", context)


def lst():
    Task.objects.all()
    context = {"key1": "value", "key2": "value"}
    return context
