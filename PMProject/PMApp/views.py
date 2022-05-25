from django.shortcuts import render
from .models import Task

# Create your views here.
def base(request):
    task = Task.objects.all()
    tasklist = []
    for i in task:
        tasklist.append({'task': i})
    context = {'tasklist': tasklist}
    return render(request, 'base.html', context)



def home(request):
    return render(request, 'home.html')