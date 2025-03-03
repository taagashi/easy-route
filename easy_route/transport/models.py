from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage


class AbstractPerson(models.Model):
    name = models.CharField(max_length=250)
    gmail = models.EmailField(max_length=250, unique=True)
    phone = models.CharField(max_length=11)

    class Meta:
        abstract = True


class Driver(AbstractPerson):
    photo = models.ImageField(upload_to='drivers/', storage=S3Boto3Storage(), null=True)

    class Meta:
        verbose_name = 'Driver'
        verbose_name_plural = 'Drivers'

    def __str__(self):
        return self.name


class Bus(models.Model):
    model = models.CharField(max_length=150)
    plate = models.CharField(max_length=7)
    capacityStudents = models.IntegerField()
    driver = models.OneToOneField('Driver', related_name='bus', on_delete=models.CASCADE)
    route = models.ForeignKey('Route', related_name='bus', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Bus"
        verbose_name_plural = "Bus"

    def __str__(self):
        return f'Ônibus {self.model}'


class Student(AbstractPerson):
    photo = models.ImageField(upload_to='students/', storage=S3Boto3Storage(), null=True)
    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.name


class Institution(models.Model):
    name = models.CharField(max_length=250)
    latitude = models.FloatField()
    longitude = models.FloatField()
    photo = models.ImageField(upload_to='institutions/', storage=S3Boto3Storage())

    class Meta:
        verbose_name = 'Institution'
        verbose_name_plural = 'Institutions'

    def __str__(self):
        return self.name


class StudentRoute(models.Model):
    student = models.ForeignKey('Student', related_name='studentRoutes', on_delete=models.CASCADE)
    route = models.ForeignKey('Route', related_name='studentRoutes', on_delete=models.CASCADE)
    going = models.BooleanField()
    back = models.BooleanField()

    class Meta:
        verbose_name = 'Student Route'
        verbose_name_plural = 'Student Routes'

    def __str__(self):
        return f'{self.student.name} na rota para {self.route.institution.name}'


class Route(models.Model):
    going = models.TimeField()
    back = models.TimeField()
    duration = models.IntegerField(default=0)
    duration_measurement = models.CharField(max_length=2, choices=[('h', 'hour'), ('m', 'minute')], default='m')
    institution = models.ForeignKey('Institution', related_name='routes', on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'

    def __str__(self):
        return f'Rota que vai para {self.institution.name}'
