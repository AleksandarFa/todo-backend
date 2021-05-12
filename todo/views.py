from django.contrib.auth.models import User
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response


from .models import Todo
from .serilizers import TodoSerializer, UserSerializer


class ShowAllTodos(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request):
        queryset = Todo.objects.filter(user=request.user)
        data = [TodoSerializer(todo).data for todo in queryset]
        return Response(data, status=status.HTTP_200_OK)


class CreateTodo(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TodoSerializer

    def create(self, request):
        new_todo = TodoSerializer(data=request.data)
        if new_todo.is_valid():
            new_todo.save()
            return Response(new_todo.data)
        return Response(new_todo.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateDestroyTodo(mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TodoSerializer

    def retrive(self, request, pk):
        current_todo = Todo.objects.get(pk=pk)
        if (request.user == current_todo.user):
            return Response(TodoSerializer(current_todo).data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        current_todo = Todo.objects.get(pk=pk)
        if (request.user == current_todo.user):
            current_todo.delete()
            return Response(TodoSerializer(current_todo).data, status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_304_NOT_MODIFIED)

    def update(self, request, pk):
        current_todo = Todo.objects.get(pk=pk)

        if (request.user == current_todo.user):
            changed_todo = TodoSerializer(current_todo, data=request.data)
            if changed_todo.is_valid():
                changed_todo.save()
                return Response(changed_todo.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_304_NOT_MODIFIED)


class RetrieveUser(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer

    def retrieve(self, request):
        current_user = request.user
        return Response(UserSerializer(current_user).data, status=status.HTTP_200_OK)
