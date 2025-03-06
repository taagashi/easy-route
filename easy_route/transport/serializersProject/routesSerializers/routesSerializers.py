from rest_framework import serializers
from transport.models import Route
from transport.serializersProject import serializers_connection

# rota apenas para POST
class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {'confirmedStudents': {'read_only': True}}
        model = Route
        fields = ['id', 'name', 'description', 'confirmedStudents', 'timeGoing', 'timeBack', 'duration', 'duration_measurement', 'institution']


# rota para GET
class RouteGetSerializer(serializers_connection.RoutesGetSerializers):
    class Meta(serializers_connection.RoutesGetSerializers.Meta):
        fields = ['id', 'name', 'description', 'confirmedStudents', 'timeGoing', 'timeBack', 'duration', 'duration_measurement', 'is_going_started', 'is_going_finished', 'is_back_started', 'is_back_finished', 'bus', 'institution']


class RouteGoingStartSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {'name': {'read_only':True}}
        model = Route
        fields = ['id', 'name', 'is_going_started']

class RouteGoingFinishSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {'name': {'read_only':True}}
        model = Route
        fields = ['id', 'name', 'is_going_finished']

class RouteBackStartSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {'name': {'read_only':True}}
        model = Route
        fields = ['id', 'name', 'is_back_started']

class RouteBackFinishSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {'name': {'read_only':True}}
        model = Route
        fields = ['id', 'name', 'is_back_finished']

    
       
        