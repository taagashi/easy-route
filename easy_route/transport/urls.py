from rest_framework.routers import DefaultRouter
from .views import DriverViewSet, BusViewSet, StudentViewSet, InstitutionViewSet, RouteViewSet

# mapeando todas as urls para CRUD basico de models

routes = DefaultRouter()
routes.register('drivers', DriverViewSet, basename='drivers')
routes.register('bus', BusViewSet, basename='bus')
routes.register('students', StudentViewSet, basename='students')
routes.register('institutions', InstitutionViewSet, basename='institutions')
routes.register('routes', RouteViewSet, basename='routes')

urlpatterns = routes.urls