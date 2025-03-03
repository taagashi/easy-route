from .views import StudentAPIView, StudentAddPhotoAPIView, DriverAPIView, DriverAddPhotoAPIView, InstitutionAPIView, InstitutionViewPhotoAPIView
from django.urls import path, include

urlpatterns = [
    path('students/', StudentAPIView.as_view(), name='students'),
    path('students/<int:pk>/photo/', StudentAddPhotoAPIView.as_view(), name='students_photo'),
    path('drivers/', DriverAPIView.as_view(), name='drivers'),
    path('drivers/<int:pk>/photo/', DriverAddPhotoAPIView.as_view(), name='drivers_photo'),
    path('institutions/', InstitutionAPIView.as_view(), name='institutions'),
    path('institutions/<int:pk>/photo/', InstitutionViewPhotoAPIView.as_view(), name='institutions_photo'),
]