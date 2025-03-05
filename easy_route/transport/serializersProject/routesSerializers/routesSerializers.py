from rest_framework import serializers
from transport.models import Route
from transport.serializersProject import serializers_connection

# rota apenas para POST
class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {'confirmedStudents': {'read_only': True}}
        model = Route
        fields = ['id', 'name', 'description', 'confirmedStudents', 'going', 'back', 'duration', 'duration_measurement', 'institution']


# rota para GET
class RouteGetSerializer(serializers_connection.RoutesGetSerializers):
    class Meta(serializers_connection.RoutesGetSerializers.Meta):
        fields = ['id', 'name', 'description', 'confirmedStudents', 'going', 'back', 'duration', 'duration_measurement', 'bus', 'institution']
    
       
        