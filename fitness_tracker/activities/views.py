from django.shortcuts import render
# activities/views.py
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from .models import Activity
from .serializers import ActivitySerializer, UserSerializer
from .permissions import IsOwner
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend


def home(request):
    return render(request, 'home.html')

# User CRUD
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Activity CRUD
class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    permission_classes = [IsOwner]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['activity_type', 'date']
    ordering_fields = ['date', 'duration', 'calories_burned']

    def get_queryset(self):
        return Activity.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def metrics(self, request):
        queryset = self.get_queryset()
        total_duration = queryset.aggregate(Sum('duration'))['duration__sum'] or 0
        total_distance = queryset.aggregate(Sum('distance'))['distance__sum'] or 0
        total_calories = queryset.aggregate(Sum('calories_burned'))['calories_burned__sum'] or 0
        return Response({
            "total_duration": total_duration,
            "total_distance": total_distance,
            "total_calories": total_calories
        })
