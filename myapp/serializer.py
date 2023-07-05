from rest_framework import serializers
from .models import ScreenShot

class ScreenShotSerializer(serializers.ModelSerializer):
    class Meta:
        model=ScreenShot
        fields='__all__'
        
    