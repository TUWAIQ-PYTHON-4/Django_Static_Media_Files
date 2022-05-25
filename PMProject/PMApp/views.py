from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def Name(request):
    name = "Lama Alkhalifah"
    return render(request, 'home.html', {"name": name})
