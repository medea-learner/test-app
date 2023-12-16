from django.shortcuts import render, get_object_or_404

from .forms import TaskForm
from .models import Task

def task(request):
    task_id = request.GET.get("task_id")
    if task_id:
        task = get_object_or_404(Task, pk=task_id)
        title = "Edit"
        if request.method == "POST":
            created_by = task.created_by
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                task.created_by = created_by
                task.save()
        else:
            form = TaskForm(instance=task)
    else:
        title = "New Task"
        if request.method == "POST":
            form = TaskForm(request.POST)
            if form.is_valid():
                task = form.save(commit=False)
                task.created_by = request.user
                task.save()
                title = "Edit"
        else:
            form = TaskForm()

    return render(
        request, 
        "task_manager/task.html", 
        dict(
            form=form, 
            title=title, 
            user_is_manager=request.user.roles.filter(name="manager").first(),
            task_id=task_id
        )
    )
