from django.shortcuts import render
from .models import Project
# Create your views here.
def index(request):
    projects = Project.objects.all()  # Fetch all projects from the database
    return render(request, 'index.html', {'projects': projects})

def about(request):
    return render(request, 'about.html')