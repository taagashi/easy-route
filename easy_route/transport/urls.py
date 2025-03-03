from .views import StudentAPIView, StudentAddPhotoAPIView, DriverAPIView, DriverAddPhotoAPIView, InstitutionAPIView, InstitutionViewPhotoAPIView
from .views import StudentListDeleteAPIView, DriverListDeleteAPIView, InstitutionListDeleteAPIView, BusAPIView, BusListDeleteAPIView, RouteAPIView, RouteListDeleteAPIView, RouteInstitutionsAPIView
from .views import BusRouteAPIView
from django.urls import path, include

urlpatterns = [
    path('students/', StudentAPIView.as_view(), name='students'),
    path('students/<int:pk>/', StudentListDeleteAPIView.as_view(), name='students_photo'),
    path('students/<int:pk>/photo/', StudentAddPhotoAPIView.as_view(), name='student_list_delete'),
   
    path('drivers/', DriverAPIView.as_view(), name='drivers'),
    path('drivers/<int:pk>/', DriverListDeleteAPIView.as_view(), name='driver_list_delete'),
    path('drivers/<int:pk>/photo/', DriverAddPhotoAPIView.as_view(), name='drivers_photo'),
    
    path('institutions/', InstitutionAPIView.as_view(), name='institutions'),
    path('institutions/<int:pk>/', InstitutionListDeleteAPIView.as_view(), name='institutions_list_delete'),
    path('institutions/<int:pk>/photo/', InstitutionViewPhotoAPIView.as_view(), name='institutions_photo'),

    path('bus/', BusAPIView.as_view(), name='bus'),
    path('bus/<int:pk>/', BusListDeleteAPIView.as_view(), name='bus_list_delete'),

    path('routes/', RouteAPIView.as_view(), name='routes'),
    path('routes/<int:pk>/', RouteListDeleteAPIView.as_view(), name='routes_list_delete'),
    path('routes/<int:pk>/institutions/', RouteInstitutionsAPIView.as_view(), name='routes_institutions'),
    path('routes/bus/<int:pk>/', BusRouteAPIView.as_view(), name='bus_route'),
]