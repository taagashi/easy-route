from rest_framework import serializers
from .models import Route, Bus, Driver, Student, Institution, StudentRoute

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = (
            'id',
            'name',
            'gmail',
            'phone',
        )

class DriverPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        extra_kwargs = {'name': {'read_only': True}}
        fields = (
            'name',
            'photo',
        )

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'id',
            'name',
            'gmail',
            'phone',
        )

class StudentPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        extra_kwargs = {'name': {'read_only': True}}
        fields = (
            'name',
            'photo',)

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = (
            'id',
            'name',
            'latitude',
            'longitude',
            'photo',
        )

class InstitutionPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        extra_kwargs = {'name': {'read_only': True}}
        fields = (
            'name',
            'photo',
        )

class StudentRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentRoute
        fields = '__all__'