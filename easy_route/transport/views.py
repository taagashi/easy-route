from django.shortcuts import render
from rest_framework import generics
from .models import Driver, Bus, Student, Institution, Route, StudentRoute
from .serializers import DriverSerializer, BusSerializer, StudentSerializer, InstitutionSerializer, StudentRouteSerializer
from .serializers import StudentPhotoSerializer, DriverPhotoSerializer, InstitutionPhotoSerializer, BusGetSerializer,RouteSerializer, RouteGetSerializer, RouteInstitutionsSerializer
from .serializers import BusRouteSerializer, StudentRouteListDeleteSerializer


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

# adicionar e listar onibus
class BusAPIView(generics.ListCreateAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer

# listar e deletar onibus
class BusListDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusGetSerializer

# adicionar e listar rotas
class RouteAPIView(generics.ListCreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

# associar onibus a uma rota
class BusRouteAPIView(generics.RetrieveUpdateAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusRouteSerializer

# listar e deletar rotas
class RouteListDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteGetSerializer

# associar rota a uma instituicao
class RouteInstitutionsAPIView(generics.RetrieveUpdateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteInstitutionsSerializer

# associar estudante a uma rota
class StudentRouteAPIView(generics.ListCreateAPIView):
    queryset = StudentRoute.objects.all()
    serializer_class = StudentRouteSerializer

# listar e deletar rotas de um estudante
class StudentRouteListDeleteAPIView(generics.ListAPIView):
    serializer_class = StudentRouteListDeleteSerializer

    def get_queryset(self):
        student_id = self.kwargs.get('pk')
        return StudentRoute.objects.filter(student_id=student_id)