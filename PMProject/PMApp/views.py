from django.shortcuts import render

# Create your views here.
from .models import Project


def Index_viwes(request):
    image=Project.objects.all()
    return render(request,"base.html",{'image':image }) 
