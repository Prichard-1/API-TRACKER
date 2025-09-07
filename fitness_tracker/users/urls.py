from django.contrib import admin
from django.urls import path, include
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Simple API status view
@api_view(['GET'])
def api_status(request):
    return Response({"status": "API is running!"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_status, name='api-root'),              # GET / → API status
    path('api/status/', api_status, name='api-status'), # GET /api/status/ → API status
    path('api/users/', include('users.urls')),         # DRF router for users
    path('api/activities/', include('activities.urls')), # placeholder for activities
    path('api/exercises/', include('wger_proxy.urls')),  # wger_proxy routes
]
