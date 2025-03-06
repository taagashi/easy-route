from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from transport.models import Route, Bus
from transport.serializersProject.routesSerializers import routesSerializers
from transport.serializersProject.driversSerializer import driversSerializers
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import FormParser, JSONParser

# adicionar rotas
class RoutePostAPIVIew(generics.CreateAPIView):
    queryset = Route.objects.all()
    serializer_class = routesSerializers.RouteSerializer
    parser_classes = [FormParser, JSONParser]

# listar rotas
class RouteListAPIView(generics.ListAPIView):
    queryset = Route.objects.all()
    serializer_class = routesSerializers.RouteGetSerializer
    parser_classes = [FormParser, JSONParser]

# listar e deletar rota
class RouteListDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Route.objects.all()
    serializer_class = routesSerializers.RouteGetSerializer
    parser_classes = [FormParser, JSONParser]



class RouteListDriversAPIView(generics.ListAPIView):
    serializer_class = driversSerializers.DriverInformationRouteSerializer
    parser_classes = [FormParser, JSONParser]

    def get_queryset(self):
        route_id = self.kwargs.get('pk')

        if route_id is None:
            return Response({'error': 'É necessário que se passe um id'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            route = Route.objects.get(pk=route_id)
            buses = Bus.objects.filter(route=route)
            drivers = [bus.driver for bus in buses]

            return drivers

        except Route.DoesNotExist:
            return Response({'error': 'Rota não encontrada'}, status=status.HTTP_404_NOT_FOUND)
            
        



