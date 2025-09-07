from rest_framework import serializers
from .models import Activity, Goal, Plan

# ===== Activity Serializer =====
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'
        read_only_fields = ['user']

    def validate(self, data):
        required = ['activity_type', 'duration', 'date']
        for field in required:
            if not data.get(field):
                raise serializers.ValidationError(f"{field} is required.")
        return data

# ===== Goal Serializer =====
class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ['id', 'title', 'description', 'target_date', 'completed', 'created_at']
        read_only_fields = ['id', 'created_at']

# ===== Plan Serializer =====
class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'created_at']
        read_only_fields = ['id', 'created_at']
