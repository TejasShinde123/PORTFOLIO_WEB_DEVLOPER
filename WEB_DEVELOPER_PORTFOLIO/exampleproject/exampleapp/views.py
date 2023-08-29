from django.shortcuts import render
from . import templates

# Create your views here.
def index(request):
    return render(request, 'templates.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    return render(request, 'contact.html')

def home(request):
    return render(request, 'home.html')
