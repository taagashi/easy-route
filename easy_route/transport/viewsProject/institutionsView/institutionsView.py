from rest_framework import generics
from transport.models import Institution
from transport.serializersProject.institutionsSerializer import institutionsSerializers

# adicionar e listar instituições
class InstitutionsPostListAPIView(generics.ListCreateAPIView):
    queryset = Institution.objects.all()
    serializer_class = institutionsSerializers.InstitutionsCRUDSerializer

# listar e deletar instituição
class InstitutionsListDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Institution.objects.all()
    serializer_class = institutionsSerializers.InstitutionsCRUDSerializer

# listar e adicionar trocar foto para uma instituição
class InstitutionsUpdateViewPhotoAPIView(generics.RetrieveUpdateAPIView):
    queryset = Institution.objects.all()
    serializer_class = institutionsSerializers.InstitutionsUpdateListPhotoSerializer