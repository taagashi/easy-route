from rest_framework import serializers
from transport.models import Student
from transport.serializersProject.studentsSerializer import studentsSerializers

class StudentsPostListSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {'photo': {'read_only': True}}
        model = Student
        fields = '__all__'

class StudentsUpdateViewPhotoSerializer(StudentsPostListSerializer):
    photo = serializers.ImageField(required=True)
    class Meta(StudentsPostListSerializer.Meta):
        extra_kwargs = {'name': {'read_only': True}}
        fields = ('id', 'name', 'photo')
