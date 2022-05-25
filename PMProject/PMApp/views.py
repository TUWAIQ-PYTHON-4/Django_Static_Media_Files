from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    all_items = Project.objects.all()
    return render(request, 'base.html', {'all_items':all_items})
