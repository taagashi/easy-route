from rest_framework import serializers
from .models import Route, Bus, Driver, Student, Institution, StudentRoute

class BusDriverNameSerializer(serializers.ModelSerializer):
    driver = serializers.CharField(source= 'driver.name')
    class Meta:
        model = Bus
        fields = (
            'driver',
            'model',
            'plate',
            'capacityStudents',
        )


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

class RouteSerializer(serializers.ModelSerializer):
    institution = InstitutionSerializer(read_only=True)
    bus = BusDriverNameSerializer(read_only=True, many=True)
    class Meta:
        extra_kwargs = {'institution': {'read_only': True}, 'bus': {'read_only': True}}
        model = Route
        fields = (
            'id',
            'going',
            'back',
            'duration',
            'duration_measurement',
            'bus',
            'institution',
        )

class RouteInstitutionsSerializer(serializers.ModelSerializer):
    route = RouteSerializer(read_only=True)
    class Meta:
        model = Route
        fields = (
            'route',
            'institution',
        )        


class RouteGetSerializer(serializers.ModelSerializer):
    institution = InstitutionSerializer(read_only=True)
    bus = BusDriverNameSerializer(read_only=True, many=True)
    class Meta:
        model = Route
        fields = (
            'id',
            'going',
            'back',
            'duration',
            'duration_measurement',
            'bus',
            'institution',
        )

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


class InstitutionPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        extra_kwargs = {'name': {'read_only': True}}
        fields = (
            'name',
            'photo',
        )


class BusSerializer(serializers.ModelSerializer):
    extra_kwargs = {'route': {'read_only': True}}
    class Meta:
        model = Bus
        fields = (
            'id',
            'model',
            'plate',
            'capacityStudents',
            'driver',
        )

class BusRouteSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {'model': {'read_only': True}}
        model = Bus
        fields = (
            'id',
            'model',
            'route',
        )

class BusGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = (
            'id',
            'model',
            'plate',
            'capacityStudents',
            'driver',
            'route',
        )


class StudentRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentRoute
        fields = '__all__'


class StudentRouteListDeleteSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    route = RouteSerializer(read_only=True)
    class Meta:
        model = StudentRoute
        fields = (
            'student',
            'route',
        )