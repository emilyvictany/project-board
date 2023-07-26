from django.shortcuts import render, redirect
from tasks.forms import TaskForm
from tasks.models import Task
from django.contrib.auth.decorators import login_required


# Create your views here.
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = TaskForm()
    context = {"form": form}
    return render(request, "tasks/create_task.html", context)


@login_required
def show_my_tasks(request):
    context = {"tasks": Task.objects.filter(assignee=request.user)}
    return render(request, "tasks/task_list.html", context)
