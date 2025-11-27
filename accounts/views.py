from rest_framework import generics, status
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
