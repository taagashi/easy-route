from django.shortcuts import render
from rest_framework import generics
from .models import Driver, Bus, Student, Institution, Route, StudentRoute
from .serializers import DriverSerializer, BusSerializer, StudentSerializer, InstitutionSerializer, RouteSerializer, StudentRouteSerializer
from .serializers import StudentPhotoSerializer, DriverPhotoSerializer, InstitutionPhotoSerializer


# adicionar e listar alunos
class StudentAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# listar e deletar aluno
class StudentListDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# adicionar e listar foto de um aluno
class StudentAddPhotoAPIView(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentPhotoSerializer

# adicionar e listar motoristas
class DriverAPIView(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

# listar e deletar motorista
class DriverListDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

# adicionar e listar foto de um motorista
class DriverAddPhotoAPIView(generics.RetrieveUpdateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverPhotoSerializer

# adicionar e listar instituicoes
class InstitutionAPIView(generics.ListCreateAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer

# listar e deletar instituicao
class InstitutionListDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer

# mudar e listar foto de uma instituicao
class InstitutionViewPhotoAPIView(generics.RetrieveUpdateAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionPhotoSerializer