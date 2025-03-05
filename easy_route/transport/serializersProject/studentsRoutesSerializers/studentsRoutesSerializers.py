from rest_framework import serializers
from transport.models import StudentRoute

class StudentRouteAddSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {'student': {'read_only':True}, 'route':{'read_only':True}}
        model = StudentRoute
        fields = ['student', 'route', 'onbus', 'going', 'back']

class StudentRouteListSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentRoute
        fields = ['student', 'route', 'onbus', 'going', 'back']


class StudentRouteUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentRoute
        fields = ['onbus', 'going', 'back']

class StudentsRouteViewStudentsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='student.name')
    id = serializers.IntegerField(source='student.id')
    institution = serializers.CharField(source='route.institution.name')
    class Meta:
        model = StudentRoute
        fields = ['id', 'name', 'going', 'back', 'onbus', 'institution']