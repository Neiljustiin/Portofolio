from django.shortcuts import render
from .models import About, Project, Contact

def index(request):
    about = About.objects.get(id=1)
    projects = Project.objects.all()
    context = {
        'about': about,
        'projects': projects,
    }
    return render(request, 'index.html', context)