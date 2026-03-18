from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Task, Category, Priority, Note, SubTask
from .forms import TaskForm


def dashboard(request):
    tasks = Task.objects.all()

    search_query = request.GET.get("q", "").strip()
    status_filter = request.GET.get("status", "").strip()
    sort_value = request.GET.get("sort", "").strip()

    if search_query:
        tasks = tasks.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    if status_filter:
        tasks = tasks.filter(status=status_filter)

    if sort_value == "newest":
        tasks = tasks.order_by("-created_at")
    elif sort_value == "oldest":
        tasks = tasks.order_by("created_at")
    elif sort_value == "due_asc":
        tasks = tasks.order_by("deadline")
    elif sort_value == "due_desc":
        tasks = tasks.order_by("-deadline")
    else:
        tasks = tasks.order_by("-created_at")

    priorities = Priority.objects.all()
    categories = Category.objects.all()

    pending_count = Task.objects.filter(status="Pending").count()
    in_progress_count = Task.objects.filter(status="In Progress").count()
    completed_count = Task.objects.filter(status="Completed").count()

    total_tasks = Task.objects.count()
    total_notes = Note.objects.count()
    total_subtasks = SubTask.objects.count()

    priority_data = []
    for priority in priorities:
        priority_data.append({
            "name": priority.name,
            "count": Task.objects.filter(priority=priority).count()
        })

    category_data = []
    for category in categories:
        category_data.append({
            "name": category.name,
            "count": Task.objects.filter(category=category).count()
        })

    context = {
        "tasks": tasks,
        "priority_data": priority_data,
        "category_data": category_data,
        "pending_count": pending_count,
        "in_progress_count": in_progress_count,
        "completed_count": completed_count,
        "total_tasks": total_tasks,
        "total_notes": total_notes,
        "total_subtasks": total_subtasks,
    }
    return render(request, "dashboard.html", context)


def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    notes = task.notes.all().order_by("-created_at")
    subtasks = task.subtasks.all().order_by("-created_at")

    completed_subtasks = subtasks.filter(status="Completed").count()
    total_subtasks_task = subtasks.count()

    context = {
        "task": task,
        "notes": notes,
        "subtasks": subtasks,
        "completed_subtasks": completed_subtasks,
        "total_subtasks_task": total_subtasks_task,
    }
    return render(request, "task_detail.html", context)


def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        subtask_titles = request.POST.getlist("subtask_title[]")
        subtask_statuses = request.POST.getlist("subtask_status[]")
        note_contents = request.POST.getlist("note_content[]")

        if form.is_valid():
            task = form.save()

            for title, status in zip(subtask_titles, subtask_statuses):
                cleaned_title = title.strip()
                if cleaned_title:
                    SubTask.objects.create(
                        parent_task=task,
                        title=cleaned_title,
                        status=status
                    )

            for content in note_contents:
                cleaned_content = content.strip()
                if cleaned_content:
                    Note.objects.create(
                        task=task,
                        content=cleaned_content
                    )

            return redirect("dashboard")
    else:
        form = TaskForm()

    context = {
        "form": form,
        "status_choices": ["Pending", "In Progress", "Completed"],
        "page_title": "Create New Task",
        "submit_label": "Save Task",
    }
    return render(request, "create_task.html", context)


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        subtask_titles = request.POST.getlist("subtask_title[]")
        subtask_statuses = request.POST.getlist("subtask_status[]")
        note_contents = request.POST.getlist("note_content[]")

        if form.is_valid():
            task = form.save()

            task.subtasks.all().delete()
            task.notes.all().delete()

            for title, status in zip(subtask_titles, subtask_statuses):
                cleaned_title = title.strip()
                if cleaned_title:
                    SubTask.objects.create(
                        parent_task=task,
                        title=cleaned_title,
                        status=status
                    )

            for content in note_contents:
                cleaned_content = content.strip()
                if cleaned_content:
                    Note.objects.create(
                        task=task,
                        content=cleaned_content
                    )

            return redirect("task_detail", task_id=task.id)
    else:
        initial_data = {
            "deadline": task.deadline.strftime("%Y-%m-%dT%H:%M")
        }
        form = TaskForm(instance=task, initial=initial_data)

    context = {
        "form": form,
        "task": task,
        "subtasks": task.subtasks.all(),
        "notes": task.notes.all(),
        "status_choices": ["Pending", "In Progress", "Completed"],
        "page_title": "Edit Task",
        "submit_label": "Update Task",
    }
    return render(request, "edit_task.html", context)


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        task.delete()
        return redirect("dashboard")

    return render(request, "delete_task.html", {"task": task})