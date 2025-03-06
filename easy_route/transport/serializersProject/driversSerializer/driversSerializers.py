from rest_framework import serializers
from transport.models import Driver

class DriverPostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'

class DriverInformationRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'name', 'gmail', 'phone']
    