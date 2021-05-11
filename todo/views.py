from django.shortcuts import render
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response


from .models import Todo
from .serilizers import TodoSerializer
# Create your views here.


class ShowAllTodos(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request):
        queryset = Todo.objects.filter(user=request.user)
        data = [TodoSerializer(todo).data for todo in queryset]
        return Response(data)
