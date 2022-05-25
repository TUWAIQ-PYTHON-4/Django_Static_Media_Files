from django.shortcuts import render
from .models import Project

def Project_list(request):
    project = Project.objects.all()
    Project_list = []
    for pub in project:
        Project_list.append({'pub':pub})
    context = {'Project_list':Project_list}
    return render(request,'base.html',context)

