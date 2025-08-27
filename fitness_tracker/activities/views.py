from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from .models import Activity
from .serializers import ActivitySerializer
from .permissions import IsOwner
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum

class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['activity_type', 'date']
    ordering_fields = ['date', 'duration', 'calories_burned']

    def get_queryset(self):
        return Activity.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def summary(self, request):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        activities = self.get_queryset()

        if start_date and end_date:
            activities = activities.filter(date__range=[start_date, end_date])

        summary = activities.aggregate(
            total_duration=Sum('duration'),
            total_distance=Sum('distance'),
            total_calories=Sum('calories_burned')
        )
        return Response(summary)



