from rest_framework import generics
from transport.models import Driver
from transport.serializersProject.driversSerializer import driversSerializers
from rest_framework.parsers import MultiPartParser, FormParser


# adicionar e listar motoristas
class DriverPostAPIView(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = driversSerializers.DriverPostListSerializer
    parser_classes = [FormParser]


# listar motoristas
class DriverListAPIView(generics.ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = driversSerializers.DriverPostListSerializer
    parser_classes = [FormParser]

# listar e deletar motorista
class DriverListDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = driversSerializers.DriverPostListSerializer
    parser_classes = [FormParser]
    
# adicionar foto para um motorista
class DriverUpdateViewPhotoAPIView(generics.RetrieveUpdateAPIView):
    queryset = Driver.objects.all()
    serializer_class = driversSerializers.DriverUpdateViewPhotoSerializer
    parser_classes = [MultiPartParser, FormParser]