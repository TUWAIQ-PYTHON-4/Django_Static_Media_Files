from django.shortcuts import render
from .models import Task,Project

def home(request):
    x = Task.objects.all()
    context = []
    for i in x:
        context.append(i)
    return render(request,"home.html",{'context':context})
def base(request):
    p = Project.objects.all()
    context = []
    for i in p:
        context.append(i)
    return render(request,'base.html',{'context':context})
