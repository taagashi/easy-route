from django.contrib import admin
from .models import Driver, Bus, Student, Institution, Route, StudentRoute

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gmail', 'phone', 'photo']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gmail', 'phone', 'photo']

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'latitude', 'longitude', 'photo']

@admin.register(StudentRoute)
class StudentRouteAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'route', 'going', 'back']

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ['id', 'going', 'back', 'duration', 'duration_measurement', 'institution']

@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ['id', 'model', 'plate', 'capacityStudents', 'driver', 'route']