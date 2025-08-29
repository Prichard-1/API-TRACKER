from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Activity
from .serializers import ActivitySerializer
from .permissions import IsOwnerOrReadOnly

class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['activity_type', 'date']

    def get_queryset(self):
        return Activity.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ActivitySummaryView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        activities = Activity.objects.filter(user=request.user)
        total_duration = sum(a.duration for a in activities)
        total_distance = sum(a.distance or 0 for a in activities)
        total_calories = sum(a.calories_burned or 0 for a in activities)

        return Response({
            "total_duration": total_duration,
            "total_distance": total_distance,
            "total_calories": total_calories
        })
