from django.urls import path
from .views import ShowAllTodos, CreateTodo, RetrieveUpdateDestroyTodo

urlpatterns = [

    path("todos/", ShowAllTodos.as_view({"get": "list"})),
    path("create-todo/",
         CreateTodo.as_view({"post": "create"})),
    path("todos/<int:pk>/",
         RetrieveUpdateDestroyTodo.as_view({"delete": "destroy", "put": "update", "get": "retrive"})),
]
