from django.db import models

class AbstractPerson(models.Model):
    name = models.CharField(max_length=250)
    gmail = models.EmailField(max_length=250)
    phone = models.CharField(max_length=11)

    class Meta:
        abstract = True


class Student(AbstractPerson):
    photo = models.ImageField(upload_to='/students')

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'


class Driver(AbstractPerson):
    photo = models.ImageField(upload_to='/drivers')

    class Meta:
        verbose_name = 'Driver'
        verbose_name_plural = 'Drivers'


class Institution(models.Model):
    name = models.CharField(max_length=250)
    latitude = models.FloatField()
    longitude = models.FloatField()
    photo = models.ImageField(upload_to='/institutions')

    class Meta:
        verbose_name = 'Institution'
        verbose_name_plural = 'Institutions'


class Route(models.Models):
    going = models.TimeField()
    back = models.TimeField()
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'


class Bus(models.Models):
    model = models.CharField(max_length=150)
    plate = models.CharField(max_length=7)
    capacityStudents = models.IntegerField()
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    students = models.ForeignKey(Student, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Bus"
        verbose_name_plural = "Bus"
