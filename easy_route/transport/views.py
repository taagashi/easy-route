from django.shortcuts import render
from rest_framework import generics
from .models import Driver, Bus, Student, Institution, Route, StudentRoute
from .serializers import DriverSerializer, BusSerializer, StudentSerializer, InstitutionSerializer, RouteSerializer, StudentRouteSerializer
from .serializers import StudentPhotoSerializer

# realizando crud basico para testes
# adicionar e listar alunos
class StudentAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# adicionar e listar foto de um aluno
class StudentAddPhotoAPIView(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentPhotoSerializer

# class DriverViewSet():
#     queryset = Driver.objects.all()
#     serializer_class = DriverSerializer

# class BusViewSet():
#     queryset = Bus.objects.all()
#     serializer_class = BusSerializer

# class StudentViewSet():
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class InstitutionViewSet():
#     queryset = Institution.objects.all()
#     serializer_class = InstitutionSerializer

# class RouteViewSet():
#     queryset = Route.objects.all()
#     serializer_class = RouteSerializer

# class StudentRouteViewSet():
#     queryset = StudentRoute.objects.all()
#     serializer_class = StudentRouteSerializer