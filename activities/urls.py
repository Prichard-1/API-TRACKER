from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActivityViewSet, ActivitySummaryView, GoalViewSet, PlanViewSet

router = DefaultRouter()
router.register(r'activities', ActivityViewSet, basename='activity')
router.register(r'goals', GoalViewSet, basename='goal')
router.register(r'plans', PlanViewSet, basename='plan')

urlpatterns = [
    # Activity summary endpoint
    path('activities/summary/', ActivitySummaryView.as_view(), name='activity-summary'),

    # Router URLs for activities, goals, and plans
    path('', include(router.urls)),
]

