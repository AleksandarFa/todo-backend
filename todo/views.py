from rest_framework import mixins, viewsets, permissions, status
from rest_framework.response import Response


from .models import Todo
from .serilizers import TodoSerializer


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
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Todo.objects.create(**serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RetrieveUpdateDestroyTodo(mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
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
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            if (request.user == serializer.validated_data['user']):
                Todo.objects.filter(pk=pk).update(**serializer.validated_data)
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_304_NOT_MODIFIED)
