from django.shortcuts import render
from .models import Task


# Create your views here.
def index(request):
    task = Task.objects.all()
    taskList = []

    for t in task:
        taskList.append({'task': t})
    context = {'taskList': taskList}
    return render(request, 'home.html', context)

def base(request):
    return render(request, 'base.html')
