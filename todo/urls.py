from django.urls import path
from .views import ShowAllTodos, CreateTodo, UpdateDestroyTodo

urlpatterns = [

    path("todos/", ShowAllTodos.as_view({"get": "list"})),
    path("create-todo/",
         CreateTodo.as_view({"post": "create"})),
    path("todo/<int:pk>/",
         UpdateDestroyTodo.as_view({"delete": "destroy", "put": "update", "get": "retrive"})),
]
