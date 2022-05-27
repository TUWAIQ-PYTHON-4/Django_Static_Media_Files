from django.shortcuts import render
from .models import Project, Task
from . import models


# Create your views here.

def index(request):
    return render(request, "base.html")


#def project(request):
    #return render(request, "base.html", context)


def task(request):
    context = Task.objects.all()
    return render(request, "base.html", {'context': context})
