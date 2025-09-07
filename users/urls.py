from django.urls import path, include
from users.views import CustomAuthToken, RegisterUser, UserDetailView
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    # Admin ViewSet endpoints
    path('api/', include(router.urls)),

    # Authentication endpoints
    path('api/login/', CustomAuthToken.as_view(), name='api-login'),
    path('api/register/', RegisterUser.as_view(), name='api-register'),
    path('api/user/', UserDetailView.as_view(), name='api-user-detail'),
]

