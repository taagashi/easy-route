from rest_framework import serializers
from transport.models import Driver

class DriverPostListSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {'photo': {'read_only': True}}
        model = Driver
        fields = '__all__'

class DriverUpdateViewPhotoSerializer(DriverPostListSerializer):
    photo = serializers.ImageField(required=True)
    class Meta(DriverPostListSerializer.Meta):
        extra_kwargs = {'name': {'read_only': True}}
        fields = ('id', 'name', 'photo')


class DriverInformationRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'name', 'gmail', 'phone']
    