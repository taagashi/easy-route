from rest_framework import generics
from transport.models import Institution
from transport.serializersProject.institutionsSerializer import institutionsSerializers
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

# adicionar instituições
class InstitutionsPostAPIView(generics.CreateAPIView):
    queryset = Institution.objects.all()
    serializer_class = institutionsSerializers.InstitutionsCRUDSerializer
    parser_classes = [FormParser, JSONParser]

# listar instituicoes
class InstitutionsListAPIView(generics.ListAPIView):
    queryset = Institution.objects.all()
    serializer_class = institutionsSerializers.InstitutionsCRUDSerializer
    parser_classes = [FormParser, JSONParser]


# listar e deletar instituição
class InstitutionsListDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Institution.objects.all()
    serializer_class = institutionsSerializers.InstitutionsCRUDSerializer
    parser_classes = [FormParser, JSONParser]

