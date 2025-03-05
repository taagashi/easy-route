from rest_framework import generics, status
from rest_framework.parsers import FormParser, JSONParser
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework import serializers
from transport.models import StudentRoute, Student, Route
from transport.serializersProject.studentsRoutesSerializers import studentsRoutesSerializers
from django.db.models import Count, Q

class StudentRouteAddtAPIView(generics.CreateAPIView):
    queryset = StudentRoute.objects.all()
    serializer_class = studentsRoutesSerializers.StudentRouteAddSerializer
    parser_classes = [FormParser, JSONParser]

    def create(self, request, *args, **kwargs):
        student_pk = self.kwargs.get('student_pk')
        route_pk = self.kwargs.get('route_pk')

        if student_pk is None:
            return Response({'error': 'Student ID is missing in the URL'}, status=status.HTTP_400_BAD_REQUEST)
        if route_pk is None:
            return Response({'error': 'Route ID is missing in the URL'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            student = Student.objects.get(pk=student_pk)
            route = Route.objects.get(pk=route_pk)
            buses = route.bus.all()
            assigned_bus = None

            for bus in buses:
                students_going = StudentRoute.objects.filter(route=route, going=True).count()
                students_back = StudentRoute.objects.filter(route=route, back=True).count()
                students_going_and_back = StudentRoute.objects.filter(route=route, going=True, back=True).count()

                total_students_in_bus = students_going + students_back + students_going_and_back

                if serializer.validated_data['going'] and serializer.validated_data['back']:  # Vai e volta
                    if total_students_in_bus < bus.capacityStudents:
                        assigned_bus = bus
                        break
                elif serializer.validated_data['going']:  # Vai apenas
                    if students_going + students_going_and_back < bus.capacityStudents:
                        assigned_bus = bus
                        break
                elif serializer.validated_data['back']:  # Volta apenas
                    if students_back + students_going_and_back < bus.capacityStudents:
                        assigned_bus = bus
                        break

            if assigned_bus is None:
                return Response({'error': 'Nao ha onibus disponível com capacidade livre nesta rota'}, status=status.HTTP_400_BAD_REQUEST)


            
            serializer.save(student=student, route=route)
            route.confirmedStudents += 1
            route.save()
            
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        except Student.DoesNotExist:
            return Response({'error': 'Estudante nao foi encontrado'}, status=status.HTTP_404_NOT_FOUND)
        except Route.DoesNotExist:
            return Response({'error': 'Rota nao foi encontrada'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': f'Error: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class StudentRouteListAPIView(generics.ListAPIView):
    serializer_class = studentsRoutesSerializers.StudentRouteListSerializer
    parser_classes = [FormParser, JSONParser]

    def get_queryset(self):
        student_pk = self.kwargs.get('pk')

        if student_pk is None:
            return Response({'Error': 'O id digitado nao existe'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            routes = StudentRoute.objects.filter(student=student_pk)
        except Exception as e:
            return Response({'error': 'id invalido'})
        
        return routes

class StudentRouteViewStudentsAPIView(generics.ListAPIView):
    serializer_class = studentsRoutesSerializers.StudentsRouteViewStudentsSerializer
    parser_classes = [FormParser, JSONParser]
    
    def get_queryset(self):
        route_pk = self.kwargs.get('pk')

        if route_pk is None:
            return Response({'Error': 'Eh necessario que a url tenha o id da rota'}, status=status.HTTP_400_BAD_REQUEST)

        route = Route.objects.get(pk=route_pk)
        
        students = StudentRoute.objects.filter(route=route)

        return students


class StudentRouteUpdateAPIView(generics.UpdateAPIView):
    queryset = StudentRoute
    serializer_class = studentsRoutesSerializers.StudentRouteUpdateSerializer
    parser_classes = [FormParser, JSONParser]

    def update(self, request, *args, **kwargs):
        
        student_pk = self.kwargs.get('student_pk')
        route_pk = self.kwargs.get('route_pk')

        if student_pk is None:
            return Response({'error':'esta faltando o id do aluno na requisicao'})
        if route_pk is None:
            return Response({'error': 'esta faltando o id da rota na requisicao'})

        student = Student.objects.get(pk=student_pk)        
        route = Route.objects.get(pk=route_pk)
        instance = StudentRoute.objects.get(student=student, route=route)

        update_serializer = self.get_serializer(instance, data=request.data, partial=True)
        update_serializer.is_valid(raise_exception=True)

        if not update_serializer.validated_data['going'] and not update_serializer.validated_data['back']:
            instance.delete()
            route.confirmedStudents = route.confirmedStudents - 1
            route.save()
            return Response({student.name: 'voce acabou de sair da rota'})
        update_serializer.save()

        response_serializer = studentsRoutesSerializers.StudentRouteListSerializer(instance)

        return Response(response_serializer.data, status=status.HTTP_200_OK)

