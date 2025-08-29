from django.urls import path, include
from users.views import CustomAuthToken, RegisterUser, UserDetailView
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from rest_framework.permissions import IsAdminUser
permission_classes = [IsAdminUser]


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    # Include router URLs first
    path('', include(router.urls)),

    # Then add custom endpoints
    path('login/', CustomAuthToken.as_view(), name='api-login'),
    path('register/', RegisterUser.as_view(), name='api-register'),
    path('user/', UserDetailView.as_view(), name='api-user-detail'),
]
