from rest_framework import serializers
from .models import Activity

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
