from django.contrib import admin
from django.urls import path, include
from .views import api_status

urlpatterns = [
    path('', api_status),  # root URL
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/activities/', include('activities.urls')),
    path('api/status/', api_status, name='api-status'),
    path('api/exercises/', include('exercises.urls')),
]

