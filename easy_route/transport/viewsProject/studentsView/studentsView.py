from rest_framework import generics
from transport.models import Student
from transport.serializersProject.studentsSerializer import studentsSerializers

#adicionar e listar alunos
class StudentPostListAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = studentsSerializers.StudentsPostListSerializer


# listar e deletar aluno
class StudentListDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = studentsSerializers.StudentsPostListSerializer


# listar e adicioar foto para um aluno
class StudentUpdateViewPhotoAPIView(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = studentsSerializers.StudentsUpdateViewPhotoSerializer