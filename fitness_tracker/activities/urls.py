from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActivityViewSet, ActivitySummaryView

router = DefaultRouter()
router.register(r'activities', ActivityViewSet, basename='activity')

urlpatterns = [
    path('summary/', ActivitySummaryView.as_view(), name='activity-summary'),
    path('', include(router.urls)),
]
