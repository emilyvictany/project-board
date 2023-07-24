from django.shortcuts import render, redirect
from projects.models import Project


# Create your views here.

# list all projects
def view_projects(request):
    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, "projects/list_projects.html", context)
