from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TodoList, Task
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context = {
        'todo_lists':TodoList.objects.filter(user=request.user)
    }
    return render(request, 'todo_app/home.html',context)
@login_required
def about(request):
    return render(request, 'todo_app/about.html')
@login_required
def addList(request):
    if request.method == "POST":
        title = request.POST['title']
        TodoList.objects.create(title=title, user=request.user)
        return redirect('todo-home')
    return render(request, 'todo_app/addlist.html')

@login_required
def todoDetailView(request, pk):
    tasks = Task.objects.filter(todo_list__id=pk)
    print(tasks)
    todo_list = TodoList.objects.get(pk=pk)
    context = {
        'tasks': tasks,
        'todo': todo_list,
    }
    return render(request, 'todo_app/todoDetail.html', context=context)

@login_required
def addTask(request, pk):
    todo_list = TodoList.objects.get(pk=pk)
    if request.method == "POST":
        task_title = request.POST['title']
        todo_list = TodoList.objects.get(pk=pk)
        task_content = request.POST['task_content']
        Task.objects.create(title=task_title, task_content=task_content, todo_list=todo_list)
        messages.success(request, "Task added successfully")
        return redirect('todo-home')
    return render(request, "todo_app/addtask.html", context={'todo_list': todo_list})
@login_required
def mark_done(request, pk):
    task = Task.objects.get(pk=pk)
    task.done = True
    task.save()
    messages.success(request, "Task marked done!")
    return redirect('todo-home')

@login_required
def delete_list(request, pk):
    TodoList.objects.get(pk=pk).delete()
    messages.success(request, "One Todo list deleted")
    return redirect('todo-home')
@login_required
def delete_task(request, pk):
    Task.objects.get(pk=pk).delete()
    messages.success(request, "Task has been deleted")
    return redirect('todo-home')