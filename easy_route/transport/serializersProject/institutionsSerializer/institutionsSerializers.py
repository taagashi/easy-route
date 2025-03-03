from rest_framework import serializers
from transport.models import Institution

class InstitutionsCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = '__all__'
        
class InstitutionsUpdateListPhotoSerializer(InstitutionsCRUDSerializer):
    class Meta(InstitutionsCRUDSerializer.Meta):
        extra_kwargs = {'name': {'read_only': True}}
        fields = ('id', 'name', 'photo')
