from rest_framework import serializers
from transport.models import Institution

class InstitutionsCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = '__all__'