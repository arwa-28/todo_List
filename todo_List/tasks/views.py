from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .models import Task
from .forms import TaskForm
from django.http import JsonResponse


@login_required
@never_cache
def tasks_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/list.html', {'tasks': tasks})


@login_required
@never_cache
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            task.user.add(request.user)
            return redirect('tasks_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})


@login_required
@never_cache
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})


@login_required
@never_cache
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks_list')
    
    return redirect('tasks_list')


@login_required
def toggle_task_complete(request):
    if request.method == "POST":
        task_id = request.POST.get("task_id")
        task = Task.objects.get(pk=task_id)
        # toggle الحالة
        task.complete = not task.complete
        task.save()
        return JsonResponse({"success": True, "complete": task.complete})
    return JsonResponse({"success": False})
