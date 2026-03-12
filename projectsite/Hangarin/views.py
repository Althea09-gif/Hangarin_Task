from django.shortcuts import render, get_object_or_404
from .models import Task, Category, Priority, Note, SubTask


def dashboard(request):
    context = {
        "task_count": Task.objects.count(),
        "category_count": Category.objects.count(),
        "priority_count": Priority.objects.count(),
        "note_count": Note.objects.count(),
        "subtask_count": SubTask.objects.count(),
        "tasks": Task.objects.all().order_by("-created_at")[:5],
    }
    return render(request, "dashboard.html", context)


def task_list(request):
    tasks = Task.objects.all().order_by("-created_at")
    return render(request, "task_list.html", {"tasks": tasks})


def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    notes = task.notes.all().order_by("-created_at")
    subtasks = task.subtasks.all().order_by("-created_at")

    context = {
        "task": task,
        "notes": notes,
        "subtasks": subtasks,
    }
    return render(request, "task_detail.html", context)