from rest_framework import generics
from transport.models import Student
from transport.serializersProject.studentsSerializer import studentsSerializers
from rest_framework.parsers import MultiPartParser, FormParser

#adicionar alunos
class StudentPostAPIView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = studentsSerializers.StudentsPostListSerializer
    parser_classes = [FormParser]

# listar alunos
class StudentListAPIView(generics.ListAPIView):
     queryset = Student.objects.all()
     serializer_class = studentsSerializers.StudentsPostListSerializer
     parser_classes = [FormParser]

# listar e deletar aluno
class StudentListDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = studentsSerializers.StudentsPostListSerializer
    parser_classes = [FormParser]


# listar e adicioar foto para um aluno
class StudentUpdateViewPhotoAPIView(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = studentsSerializers.StudentsUpdateViewPhotoSerializer
    parser_classes = [MultiPartParser, FormParser]