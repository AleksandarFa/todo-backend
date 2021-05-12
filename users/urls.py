from django.urls import path
from .views import RetrieveUser

urlpatterns = [
    path("me/", RetrieveUser.as_view({"get": "retrieve"})),
]
