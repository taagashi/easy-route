from .views import StudentAPIView, StudentAddPhotoAPIView
from django.urls import path, include

urlpatterns = [
    path('students/', StudentAPIView.as_view(), name='students'),
    path('students/<int:pk>/photo/', StudentAddPhotoAPIView.as_view(), name='students_photo'),
]