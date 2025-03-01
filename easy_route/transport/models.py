from django.db import models

# Um onibus tem apenas um motorista e cada motorista tem apenas um onibus
# Um onibus pode ter varios alunos, mas cada aluno pode ter apenas um onibus
# Um onibus tem apenas uma rota e uma rota pode ter varios onibus
# Uma rota tem apenas uma instituicao e uma instituicao pode ter varias rotas

class AbstractPerson(models.Model):
    name = models.CharField(max_length=250)
    gmail = models.EmailField(max_length=250)
    phone = models.CharField(max_length=11)

    class Meta:
        abstract = True


class Driver(AbstractPerson):
    photo = models.ImageField(upload_to='/drivers')

    class Meta:
        verbose_name = 'Driver'
        verbose_name_plural = 'Drivers'

    def __str__(self):
        return self.name
    

class Bus(models.Model):
    model = models.CharField(max_length=150)
    plate = models.CharField(max_length=7)
    capacityStudents = models.IntegerField()
    driver = models.OneToOneField(Driver, related_name='bus', on_delete=models.CASCADE)
    route = models.ForeignKey('Route', related_name='bus', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Bus"
        verbose_name_plural = "Bus"

    def __str__(self):
        return f'Ônibus {self.model}'


class Student(AbstractPerson):
    photo = models.ImageField(upload_to='/students')
    bus = models.ForeignKey(Bus, related_name='students', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.name


class Institution(models.Model):
    name = models.CharField(max_length=250)
    latitude = models.FloatField()
    longitude = models.FloatField()
    photo = models.ImageField(upload_to='/institutions')

    class Meta:
        verbose_name = 'Institution'
        verbose_name_plural = 'Institutions'

    def __str__(self):
        return self.name


class Route(models.Model):
    going = models.TimeField()
    back = models.TimeField()
    institution = models.ForeignKey(Institution, related_name='routes', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'

    def __str__(self):
        return f'Rota que vai para {self.institution.name}'
