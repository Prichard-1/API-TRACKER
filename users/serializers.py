from rest_framework import serializers
from django.contrib.auth.models import User
from activities.serializers import ActivitySerializer

class UserSerializer(serializers.ModelSerializer):
    activities = ActivitySerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'activities']
