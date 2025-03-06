from django.contrib import admin
from .models import Driver, Bus, Student, Institution, Route, StudentRoute

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gmail', 'phone']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gmail', 'phone']

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'latitude', 'longitude']

@admin.register(StudentRoute)
class StudentRouteAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'route', 'going']

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'confirmedStudents', 'timeGoing', 'timeBack', 'duration', 'duration_measurement', 'is_going_started', 'is_going_finished', 'is_back_started', 'is_back_finished', 'institution']

@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ['id', 'model', 'plate', 'capacityStudents', 'driver', 'route']