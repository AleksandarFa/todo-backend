from django.urls import path
from .views import ShowAllTodos

urlpatterns = [

    path("todos/", ShowAllTodos.as_view({"get": "list"})),

]
