from .serializers import RegisterSerializer
from rest_framework import mixins, viewsets, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import User


class RegisterUser(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (permissions.AllowAny, )
    serializer_class = RegisterSerializer

    def create(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        current_user = User.objects.create(username=serializer.validated_data['username'],
                                           email=serializer.validated_data["email"],
                                           first_name=serializer.validated_data["first_name"],
                                           last_name=serializer.validated_data["last_name"],
                                           )
        current_user.set_password(serializer.validated_data['password'])
        current_user.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
