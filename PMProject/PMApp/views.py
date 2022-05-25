from django.shortcuts import render
from . import models

# Create your views here.

def index(request):
    context = models.Project.objects.all()
    return render(request, 'index.html',{"context":context})
