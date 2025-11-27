from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from .forms import TodoForm
from .models import Todo


def register(request):
    if request.user.is_authenticated:
        return redirect("todoapp:todo-list")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("todoapp:todo-list")
    else:
        form = UserCreationForm()

    return render(request, "todoapp/register.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("todoapp:todo-list")

    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        return redirect("todoapp:todo-list")

    return render(request, "todoapp/login.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    return redirect("todoapp:login")


@login_required
def todo_list(request):
    todos = request.user.todos.order_by("-created_at")

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect("todoapp:todo-list")
    else:
        form = TodoForm()

    return render(
        request,
        "todoapp/todo_list.html",
        {
            "todos": todos,
            "form": form,
        },
    )


@login_required
def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("todoapp:todo-list")
    else:
        form = TodoForm(instance=todo)

    return render(
        request,
        "todoapp/todo_edit.html",
        {
            "todo": todo,
            "form": form,
        },
    )


@login_required
@require_http_methods(["POST"])
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.delete()
    return redirect("todoapp:todo-list")
