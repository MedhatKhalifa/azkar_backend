from rest_framework import serializers
from .models import Azkar, DatabaseVersion

class AzkarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Azkar
        fields = '__all__'

class DatabaseVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatabaseVersion
        fields = ['version', 'updated_at']
