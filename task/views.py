from django.shortcuts import render, redirect
from django.utils import timezone

from task.models import Task, Category, Priority
from task.forms import TaskForm, TaskFilterForm


def list_tasks(request):
    today = timezone.now().date()

    form = TaskFilterForm(request.GET or None)
    tasks = Task.objects.all()

    if form.is_valid():
        search_task = form.cleaned_data.get('search_task')
        category = form.cleaned_data.get('category')
        priority = form.cleaned_data.get('priority')

        if search_task:
            tasks = tasks.filter(title__icontains=search_task)
        if category:
            tasks = tasks.filter(category=category)
        if priority:
            tasks = tasks.filter(priority=priority)

    return render(request, 'task/task_list.html', {
        'tasks': tasks,
        'today': today,
        'form': form,
    })


def tasks_by_category(request, category_id):
    category = Category.objects.get(id=category_id)
    today = timezone.now().date()

    form = TaskFilterForm(request.GET or None)
    tasks = Task.objects.filter(category=category)

    if form.is_valid():
        search_task = form.cleaned_data.get('search_task')
        category = form.cleaned_data.get('category')
        priority = form.cleaned_data.get('priority')

        if search_task:
            tasks = tasks.filter(title__icontains=search_task)
        if category:
            tasks = tasks.filter(category=category)
        if priority:
            tasks = tasks.filter(priority=priority)

    return render(request, 'task/task_list.html', {
        'tasks': tasks,
        'today': today,
        'form': form,
    })


def tasks_by_priority(request, priority_id):
    priority = Priority.objects.get(id=priority_id)
    today = timezone.now().date()

    form = TaskFilterForm(request.GET or None)
    tasks = Task.objects.filter(priority=priority)

    if form.is_valid():
        search_task = form.cleaned_data.get('search_task')
        category = form.cleaned_data.get('category')
        priority = form.cleaned_data.get('priority')

        if search_task:
            tasks = tasks.filter(title__icontains=search_task)
        if category:
            tasks = tasks.filter(category=category)
        if priority:
            tasks = tasks.filter(priority=priority)

    return render(request, 'task/task_list.html', {
        'tasks': tasks,
        'today': today,
        'form': form,
    })


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-task')
    else:
        form = TaskForm()
        return render(request, 'task/create_task.html', {'form': form})


def edit_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('list-task')
    else:
        form = TaskForm(instance=task)
        return render(request, 'task/edit_task.html', {'form': form})


def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('list-task')


def toggle_task_status(request, pk):
    task = Task.objects.get(pk=pk)
    task.status = True
    task.save()
    return redirect('list-task')


def list_categories(request):
    categories = Category.objects.all()
    return render(request, 'task/list_categories.html', {'categories': categories})


def list_priorities(request):
    priorities = Priority.objects.all()
    return render(request, 'task/list_priorities.html', {'priorities': priorities})