from django.urls import path
from .views import ExerciseSearchView, ExerciseRootView

urlpatterns = [
    path('', ExerciseRootView.as_view(), name='exercise-root'),
    path('search/', ExerciseSearchView.as_view(), name='exercise-search'),
]
