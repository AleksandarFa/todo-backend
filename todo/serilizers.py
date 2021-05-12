from rest_framework import serializers
from rest_framework.views import get_view_name
from .models import Todo
from users.serializers import UserSerializer


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = "__all__"
