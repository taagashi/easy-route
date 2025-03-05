from django.urls import path, include

from transport.viewsProject.studentsView import studentsView
from transport.viewsProject.driversView import driversView
from transport.viewsProject.institutionsView import institutionsView
from transport.viewsProject.busView import busView
from transport.viewsProject.routesView import routesView
from transport.viewsProject.studentsRoutesView import studentsRoutesView

urlpatterns = [
    # cadastrar e listar alunos : FEITO
    path('students/', studentsView.StudentPostAPIView.as_view(), name='students'),

    # listar alunos : FEITO
    path('students/list/', studentsView.StudentListAPIView.as_view(), name='students_list'),
    
    # listar aluno e deletar : FEITO
    path('students/list/<int:pk>/', studentsView.StudentListDeleteAPIView.as_view(), name='students_list_delete'),
    
    # adicionar foto para um aluno : FEITO
    path('students/list/<int:pk>/photo/', studentsView.StudentUpdateViewPhotoAPIView.as_view(), name='student_photo'),
    
    # cadastro de aluno em uma rota : FEITO
    path('students/list/<int:student_pk>/routes/list/<int:route_pk>/', studentsRoutesView.StudentRouteAddtAPIView.as_view(), name='student_route_list'),
    
    # listar rotas de um aluno : FEITO
    path('students/list/<int:pk>/routes/', studentsRoutesView.StudentRouteListAPIView.as_view(), name='student_route_list_routes'),

    # Atualizar ida e volta de um aluno em uma rota : FEITO
    path('students/list/<int:student_pk>/routes/<int:route_pk>/update/', studentsRoutesView.StudentRouteUpdateAPIView.as_view(), name='student_route_update'),
   
   
   
    # adicionar motoristas : FEITO
    path('drivers/', driversView.DriverPostAPIView.as_view(), name='drivers'),
    
    #listar motoristas : FEITO
    path('drivers/list/', driversView.DriverListAPIView.as_view(), name='drivers_list'),
    
    # listar e deletar motorista : FEITO
    path('drivers/list/<int:pk>/', driversView.DriverListDeleteAPIView.as_view(), name='driver_list_delete'),
   
    # adicionar foto para um motorista : FEITO
    path('drivers/list/<int:pk>/photo/', driversView.DriverUpdateViewPhotoAPIView.as_view(), name='drivers_photo'),
    
   
   
   
    # adicionar instituicoes : FEITO
    path('institutions/', institutionsView.InstitutionsPostAPIView.as_view(), name='institutions'),

    # listar instituticoes : FEITO
    path('institutions/list/', institutionsView.InstitutionsListAPIView.as_view(), name='institutions_list'),

    # listar e deletar instituicoes : FEITO
    path('institutions/list/<int:pk>/', institutionsView.InstitutionsListDeleteAPIView.as_view(), name='institutions_list_delete'),
   
    # atualizar foto de instituicao : FEITO
    path('institutions/list/<int:pk>/photo/', institutionsView.InstitutionsUpdateViewPhotoAPIView.as_view(), name='institutions_photo'),

   
   
    # adicionar onibus(plural) : FEITO
    path('bus/', busView.BusPostAPIView.as_view(), name='bus'),
   
    # listar onibus(plural) : FEITO
    path('bus/list', busView.BusListAPIView.as_view(), name='bus_list'),
   
    # listar e deletar onibus(individual) : FEITO
    path('bus/list/<int:pk>/', busView.BusListDeleteAPIView.as_view(), name='bus_list_delete'),
    
    # # atribuir rota para um onibus -> isso ja ta sendo feito ao adicionar o onibus
    # path('bus/list/<int:pk>/routes', busView.BusAddListRouteAPIView.as_view(), name='bus_route'),



    # adicionar rotas: FEITO
    path('routes/', routesView.RoutePostAPIVIew.as_view(), name='routes'),
    
    # listar rotas : FEITO
    path('routes/list/', routesView.RouteListAPIView.as_view(), name='routes_list'),
   
    # listar e deletar rota : FEITO
    path('routes/list/<int:pk>/', routesView.RouteListDeleteAPIView.as_view(), name='routes_list_delete'),

    # listar estudantes cadastrados em uma rota
    path('routes/list/<int:pk>/students', studentsRoutesView.StudentRouteViewStudentsAPIView.as_view(), name='routes_list_students'),



    
]