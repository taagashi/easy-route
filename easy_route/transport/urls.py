from .views import StudentAPIView, StudentAddPhotoAPIView, DriverAPIView, DriverAddPhotoAPIView, InstitutionAPIView, InstitutionViewPhotoAPIView
from .views import StudentListDeleteAPIView, DriverListDeleteAPIView, InstitutionListDeleteAPIView, BusAPIView, BusListDeleteAPIView, RouteAPIView, RouteListDeleteAPIView, RouteInstitutionsAPIView
from .views import BusRouteAPIView, StudentRouteAPIView, StudentRouteListDeleteAPIView
from django.urls import path, include

from transport.viewsProject.studentsView import studentsView
urlpatterns = [
    # cadastrar e listar alunos : FEITO
    path('students/', studentsView.StudentPostListAPIView.as_view(), name='students'),
    # listar aluno e deletar : FEITO
    path('students/<int:pk>/', studentsView.StudentListDeleteAPIView.as_view(), name='students_list_delete'),
    # adicionar foto para um aluno : FEITO
    path('students/<int:pk>/photo/', studentsView.StudentUpdateViewPhotoAPIView.as_view(), name='student_photo'),
    # cadastro de aluno em uma rota
    path('students/<int:students_pk>/routes/<int:routes_pk>/', StudentRouteAPIView.as_view(), name='student_route'),
    # listar rotas de um aluno
    path('students/<int:pk>/routes/', StudentRouteListDeleteAPIView.as_view(), name='student_routes'),
   
    # adicionar e listar motoristas
    path('drivers/', DriverAPIView.as_view(), name='drivers'),
    # listar e deletar motorista
    path('drivers/<int:pk>/', DriverListDeleteAPIView.as_view(), name='driver_list_delete'),
    # adicionar foto para um motorista
    path('drivers/<int:pk>/photo/', DriverAddPhotoAPIView.as_view(), name='drivers_photo'),
    
    # adicionar e listar instituicoes
    path('institutions/', InstitutionAPIView.as_view(), name='institutions'),
    # listar e deletar instituicoes
    path('institutions/<int:pk>/', InstitutionListDeleteAPIView.as_view(), name='institutions_list_delete'),
    # atualizar foto de instituicao
    path('institutions/<int:pk>/photo/', InstitutionViewPhotoAPIView.as_view(), name='institutions_photo'),

    # adicionar e listar onibus
    path('bus/', BusAPIView.as_view(), name='bus'),
    # listar e deletar onibus
    path('bus/<int:pk>/', BusListDeleteAPIView.as_view(), name='bus_list_delete'),
    # atribuir rota para um onibus
    path('bus/<int:pk>/routes', BusRouteAPIView.as_view(), name='bus_route'),

    # adicionar e listar rotas
    path('routes/', RouteAPIView.as_view(), name='routes'),
    # listar e deletar rotas
    path('routes/<int:pk>/', RouteListDeleteAPIView.as_view(), name='routes_list_delete'),
    # adicionar instituicao para rota
    path('routes/<int:pk>/institutions/', RouteInstitutionsAPIView.as_view(), name='routes_institutions'),
    
]