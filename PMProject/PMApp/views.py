from django.shortcuts import render
from .models import Task

# Create your views here.
def index(request):
    task = Task.objects.all()
    tasklist = []
    for i in task:
        tasklist.append({'task': i})
    context = {'tasklist': tasklist}
    return render(request, 'index.html', context)



def home(request):
    return render(request, 'home.html')
