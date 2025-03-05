from rest_framework import serializers
from transport.models import Bus, Route
from transport.serializersProject import serializers_connection

class BusPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ['id', 'model', 'plate', 'capacityStudents', 'driver', 'route']

class BusGetSerializer(serializers_connection.BusGetSerializer):
    class Meta(serializers_connection.BusGetSerializer.Meta):
        fields = ['id', 'model', 'plate', 'capacityStudents', 'driver', 'route']

