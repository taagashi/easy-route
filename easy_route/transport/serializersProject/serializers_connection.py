from rest_framework import serializers
from transport.models import Bus, Route
from transport.serializersProject.institutionsSerializer import institutionsSerializers

# ESSE SERIALIZERS VAO SERVIR PARA SERIALIZAR A ROTA EM GETS
class BusComposeRouteSerializer(serializers.ModelSerializer):
    driver = serializers.CharField(source='driver.name')
    
    class Meta:
        model = Bus
        fields = (
            'id',
            'driver',
            'model',
            'plate',
            'capacityStudents',
        )


class RoutesGetSerializers(serializers.ModelSerializer):
    institution = institutionsSerializers.InstitutionsCRUDSerializer()
    bus = BusComposeRouteSerializer(many=True)
    class Meta:
        model = Route
        fields = ['id', 'name', 'description', 'confirmedStudents', 'going', 'back', 'duration', 'duration_measurement', 'bus', 'institution']



# ESSES SERIALIZERS VAO SERVIR PARA SERIALIZAR O ONIBUS EM GETS
class RoutesComposeBusSerializer(serializers.ModelSerializer):
    institution = institutionsSerializers.InstitutionsCRUDSerializer()
    class Meta:
        model = Route
        fields = ['id', 'name', 'description', 'confirmedStudents', 'going', 'back', 'duration', 'duration_measurement', 'institution']


class BusGetSerializer(serializers.ModelSerializer):
    driver = serializers.CharField(source='driver.name')
    route = RoutesComposeBusSerializer()
    class Meta:
        model = Bus
        fields = ['id', 'model', 'plate', 'capacityStudents', 'driver', 'route']





    