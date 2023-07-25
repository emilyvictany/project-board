from django.shortcuts import render, redirect, get_object_or_404
from projects.models import Project
from django.contrib.auth.decorators import login_required


# Create your views here.

# list all projects
@login_required
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        "projects": projects
    }
    return render(request, "projects/list_projects.html", context)


@login_required
def show_project(request, id):
    context = {
        "project": get_object_or_404(Project, id=id)
    }
    return render(request, "projects/project_detail.html", context)
