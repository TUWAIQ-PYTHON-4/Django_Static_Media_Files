from django.shortcuts import render

# Create your views here.
from .models import Task


def admin_object(request):
    x = Task.objects.all()
    Tasks = []
    for i in x:
        Tasks.append(i)

    return render(request, "base.html", {"Tasks": Tasks})

