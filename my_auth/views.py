from .serializers import RegisterSerializer
from rest_framework import mixins, viewsets, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import User


class RegisterUser(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny, )
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
