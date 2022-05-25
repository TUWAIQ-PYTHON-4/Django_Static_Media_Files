from django.shortcuts import render
from .models import Project


# Create your views here.

def Pmp(request):
    return render(request, 'home.html', {})


def project_list(request):
    project = Project.objects.all()
    project_list = []

    for project in project:
        project_list.append({'project': project})

    context = {'project_list': project_list}
    return render(request, 'home.html', context)
