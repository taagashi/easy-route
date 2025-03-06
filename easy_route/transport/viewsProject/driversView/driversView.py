from rest_framework import generics
from rest_framework.exceptions import ValidationError
from transport.models import Driver, Route, Bus, StudentRoute
from transport.serializersProject.driversSerializer import driversSerializers
from transport.serializersProject.routesSerializers import routesSerializers
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework import status


# adicionar e listar motoristas
class DriverPostAPIView(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = driversSerializers.DriverPostListSerializer
    parser_classes = [FormParser, JSONParser]


# listar motoristas
class DriverListAPIView(generics.ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = driversSerializers.DriverPostListSerializer
    parser_classes = [FormParser, JSONParser]

# listar e deletar motorista
class DriverListDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = driversSerializers.DriverPostListSerializer
    parser_classes = [FormParser, JSONParser]
    
# adicionar foto para um motorista
class DriverUpdateViewPhotoAPIView(generics.RetrieveUpdateAPIView):
    queryset = Driver.objects.all()
    serializer_class = driversSerializers.DriverUpdateViewPhotoSerializer
    parser_classes = [MultiPartParser, FormParser]

# lista rota de um motorista
class DriverListRoute(generics.RetrieveAPIView):
    serializer_class = routesSerializers.RouteSerializer
    parser_classes = [FormParser, JSONParser]
    def get_queryset(self):
        driver_id = self.kwargs.get('pk')
        
        if driver_id is None:
            return Response({'error': 'O id digitado nao existe'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            driver = Driver.objects.get(pk=driver_id)
            bus = driver.bus
            routes = Route.objects.filter(bus=bus.id)    
            return routes
        except Driver.DoesNotExist:
            return Response({'Error': 'nao foi encontrado motorista com esse id'}, status=status.HTTP_404_NOT_FOUND)
        except Bus.DoesNotExist: # adicionamos essa excecao
            return Response({'error': 'Nao ha nenhum onibus para este motorista'}, status=status.HTTP_404_NOT_FOUND)
        


# motorista inicia rote
class DriverGoingRouteAPIView(generics.UpdateAPIView):
    serializer_class = routesSerializers.RouteGoingStartSerializer
    parser_classes = [FormParser, JSONParser]

    def get_queryset(self):
        return Route.objects.all()

    def update(self, request, *args, **kwargs):
        driver_id = self.kwargs.get('pk')

        if driver_id is None:
            return Response({'error': 'O id do motorista nao foi encontrado'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            driver = Driver.objects.get(pk=driver_id)
            bus = driver.bus
            instance = Route.objects.get(bus=bus.id) # <<--- usar get() em vez de filter() para obter uma instancia Route

            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Driver.DoesNotExist:
            return Response({'Error': 'nao foi encontrado motorista com esse id'}, status=status.HTTP_404_NOT_FOUND)
        except Bus.DoesNotExist:
            return Response({'error': 'Nao ha nenhum onibus para este motorista'}, status=status.HTTP_404_NOT_FOUND)
        except Route.DoesNotExist:
            return Response({'error': 'Nao foi encontrada rota para este onibus'}, status=status.HTTP_404_NOT_FOUND)
        except ValidationError:
            return Response({'error': 'valor invalido passado para o campo'}, status=status.HTTP_400_BAD_REQUEST)


# motorista sinaliza que a rota da ida foi finalizada
class DriverStartFinishedRouteAPIView(generics.UpdateAPIView):
     serializer_class = routesSerializers.RouteGoingFinishSerializer
     parser_classes = [FormParser, JSONParser]

     def get_queryset(self):
        return Route.objects.all()


     def update(self, request, *args, **kwargs):
        driver_id = self.kwargs.get('pk')

        if driver_id is None:
            return Response({'error': 'O id do motorista nao foi encontrado'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            driver = Driver.objects.get(pk=driver_id)
            bus = driver.bus
            instance = Route.objects.get(bus=bus.id)

            students = StudentRoute.objects.filter(route=instance, going=True)

            instance.confirmedStudents -= students.count()
            students.delete()
            instance.save()

            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Driver.DoesNotExist:
            return Response({'Error': 'nao foi encontrado motorista com esse id'}, status=status.HTTP_404_NOT_FOUND)
        except Bus.DoesNotExist:
            return Response({'error': 'Nao ha nenhum onibus para este motorista'}, status=status.HTTP_404_NOT_FOUND)
        except Route.DoesNotExist:
            return Response({'error': 'Nao foi encontrada rota para este onibus'}, status=status.HTTP_404_NOT_FOUND)
        except ValidationError:
            return Response({'error': 'valor invalido passado para o campo'}, status=status.HTTP_400_BAD_REQUEST)


# motorista inicia parte de volta da rota
class DriverBackRouteAPIView(generics.UpdateAPIView):
    serializer_class = routesSerializers.RouteBackStartSerializer
    parser_classes = [FormParser, JSONParser]

    def get_queryset(self):
        return Route.objects.all()

    def update(self, request, *args, **kwargs):
        driver_id = self.kwargs.get('pk')

        if driver_id is None:
            return Response({'error': 'O id do motorista nao foi encontrado'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            driver = Driver.objects.get(pk=driver_id)
            bus = driver.bus
            instance = Route.objects.get(bus=bus.id)

            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Driver.DoesNotExist:
            return Response({'Error': 'nao foi encontrado motorista com esse id'}, status=status.HTTP_404_NOT_FOUND)
        except Bus.DoesNotExist:
            return Response({'error': 'Nao ha nenhum onibus para este motorista'}, status=status.HTTP_404_NOT_FOUND)
        except Route.DoesNotExist:
            return Response({'error': 'Nao foi encontrada rota para este onibus'}, status=status.HTTP_404_NOT_FOUND)



# motorista sinaliza que o onibus finalizou a rota da volta, assim fechando a rota e liberando alunos da volta
class DriverBackFinishedAPIView(generics.UpdateAPIView): #retornamos para UpdateAPIView
    serializer_class = routesSerializers.RouteBackFinishSerializer
    parser_classes = [FormParser, JSONParser]

    def get_queryset(self):
        return Route.objects.all()

    def update(self, request, *args, **kwargs): #voltamos para update
        driver_id = self.kwargs.get('pk')

        if driver_id is None:
            return Response({'error': 'O id do motorista nao foi encontrado'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            driver = Driver.objects.get(pk=driver_id)
            bus = driver.bus
            instance = Route.objects.get(bus=bus.id)

            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save() #vamos atualizar o is_back_finished

            # deletar alunos que estao voltando
            students = StudentRoute.objects.filter(route=instance, back=True)
            instance.confirmedStudents -= students.count()
            students.delete()

            instance.save() #vamos salvar o numero de students que foram removidos
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Driver.DoesNotExist:
            return Response({'Error': 'nao foi encontrado motorista com esse id'}, status=status.HTTP_404_NOT_FOUND)
        except Bus.DoesNotExist:
            return Response({'error': 'Nao ha nenhum onibus para este motorista'}, status=status.HTTP_404_NOT_FOUND)
        except Route.DoesNotExist:
            return Response({'error': 'Nao foi encontrada rota para este onibus'}, status=status.HTTP_404_NOT_FOUND)
        except ValidationError:
            return Response({'error': 'valor invalido passado para o campo'}, status=status.HTTP_400_BAD_REQUEST)
