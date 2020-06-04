from django.shortcuts import render, redirect
from .models import TodoList
from . forms import ListForm
from django.contrib import messages


def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = TodoList.objects.all()
            messages.success(
                request, ('A new item has been added to the list.'))
            return render(request, 'todo/home.html', {'all_items': all_items})
    else:
        all_items = TodoList.objects.all()
        return render(request, 'todo/home.html', {'all_items': all_items})


def delete(request, list_id):
    item = TodoList.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('The item has been deleted successfully.'))
    return redirect('todo_home')


def mark_complete(request, list_id):
    item = TodoList.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('todo_home')


def mark_open(request, list_id):
    item = TodoList.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('todo_home')


def edit_item(request, list_id):
    if request.method == 'POST':
        item = TodoList.objects.get(pk=list_id)

        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(
                request, ('The item has been edited successfully.'))
            return redirect('todo_home')
    else:
        item = TodoList.objects.get(pk=list_id)
        return render(request, 'todo/edit_item.html', {'item': item})
