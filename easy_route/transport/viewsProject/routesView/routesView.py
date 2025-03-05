from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from transport.models import Route
from transport.serializersProject.routesSerializers import routesSerializers
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import FormParser

# adicionar rotas
class RoutePostAPIVIew(generics.CreateAPIView):
    queryset = Route.objects.all()
    serializer_class = routesSerializers.RouteSerializer
    parser_classes = [FormParser]

# listar rotas
class RouteListAPIView(generics.ListAPIView):
    queryset = Route.objects.all()
    serializer_class = routesSerializers.RouteGetSerializer
    parser_classes = [FormParser]

# listar e deletar rota
class RouteListDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Route.objects.all()
    serializer_class = routesSerializers.RouteGetSerializer
    parser_classes = [FormParser]

