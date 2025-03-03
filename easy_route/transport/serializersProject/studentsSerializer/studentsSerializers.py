from rest_framework import serializers
from transport.models import Student

class StudentPostListSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {'photo': {'read_only': True}}
        model = Student
        fields = '__all__'

class StudentsUpdateViewPhotoSerializer(StudentPostListSerializer):
    photo = serializers.ImageField(required=True)
    class Meta(StudentPostListSerializer.Meta):
        extra_kwargs = {'name': {'read_only': True}}
        fields = ('id', 'name', 'photo')