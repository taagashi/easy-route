from rest_framework import generics
from transport.models import Driver
from transport.serializersProject.drivers import driversSerializers

# adicionar e listar motoristas
class DriverPostListAPIView(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = driversSerializers.DriverPostListSerializer

# lsitar e deletar motorista
class DriverListDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = driversSerializers.DriverPostListSerializer

# adicionar foto para um motorista
class DriverUpdateViewPhotoAPIView(generics.RetrieveUpdateAPIView):
    queryset = Driver.objects.all()
    serializer_class = driversSerializers.DriverUpdateViewPhotoSerializer