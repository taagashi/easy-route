from rest_framework import generics
from transport.models import Bus
from transport.serializersProject.busSerializers import busSerializers
from rest_framework.parsers import FormParser, JSONParser
from rest_framework.response import Response  # <<--- ADICIONE ESTA LINHA


# adicionar onibus(plural)
class BusPostAPIView(generics.CreateAPIView):
    queryset = Bus.objects.all()
    serializer_class = busSerializers.BusPostSerializer
    parser_classes = [FormParser, JSONParser]


# listar onibus(plural)
class BusListAPIView(generics.ListAPIView):
    queryset = Bus.objects.all()
    serializer_class = busSerializers.BusGetSerializer
    parser_classes = [FormParser, JSONParser]

# listar onibus(individual) e deletar
class BusListDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Bus.objects.all()
    serializer_class = busSerializers.BusGetSerializer
    parser_classes = [FormParser, JSONParser]


