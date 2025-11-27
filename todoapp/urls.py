from django.urls import path

from . import views


app_name = "todoapp"

urlpatterns = [
    path("", views.todo_list, name="todo-list"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("todos/<int:pk>/edit/", views.todo_edit, name="todo-edit"),
    path("todos/<int:pk>/delete/", views.todo_delete, name="todo-delete"),
]

