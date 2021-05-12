from rest_framework import mixins, viewsets, permissions, status
from rest_framework.response import Response
from .serializers import UserSerializer


class RetrieveUser(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer

    def retrieve(self, request):
        current_user = request.user
        return Response(UserSerializer(current_user).data, status=status.HTTP_200_OK)
