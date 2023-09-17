from rest_framework import serializers
from .models import Ball


class BallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ball
        fields = '__all__'
