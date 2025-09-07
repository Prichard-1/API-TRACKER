# users/views.py
from rest_framework import generics, viewsets, permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer

# Registration endpoint
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # anyone can register

# User management endpoint
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]  # only logged-in users

