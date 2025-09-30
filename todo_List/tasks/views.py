from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task

# عرض كل التاسكات
@login_required
def tasks_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/list.html', {'tasks': tasks})

# إنشاء تاسك جديد
@login_required
def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        complete = request.POST.get('complete') == 'on'

        task = Task.objects.create(title=title, description=description, complete=complete)
        task.user.add(request.user)  # ربط التاسك باليوزر الحالي
        return redirect('tasks_list')

    return render(request, 'tasks/task_form.html')

# تعديل تاسك
@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.complete = request.POST.get('complete') == 'on'
        task.save()
        return redirect('tasks_list')

    return render(request, 'tasks/task_form.html', {'task': task})

# حذف تاسك
@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks_list')

    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
