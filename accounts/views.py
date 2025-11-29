from rest_framework import generics, status
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema


class RegisterUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = []

    @swagger_auto_schema(
        operation_summary="Register a new user",
        operation_description=(
            "Create a new user account.\n\n"
            "Send username, email, and password in JSON body."
        ),
        request_body=UserSerializer,
        responses={
            201: UserSerializer,
            400: "Validation error"
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
