from django.db import models
from simple_history.models import HistoricalRecords

class Sexo(models.Model):
    id=models.AutoField(primary_key=True)
    sexo=models.CharField('Sexo (*)', max_length =10,blank=False,null=False)
    def __str__(self):
        return self.sexo 

class Persona(models.Model):
    id =  models.AutoField(primary_key = True)
    cuit=models.CharField('Cuit (*)',max_length=11, blank=False, null=False)
    dni=models.CharField('DNI (*)',max_length=10, blank=False, null=False)
    nombre=models.CharField('Nombre (*)',max_length=20,blank = False, null = False)
    apellido = models.CharField('Apellido (*)',max_length=50,blank = False, null = True)
    domicilio=models.CharField('Domicilio (*)',max_length=50,blank = False, null = True)
    email=models.EmailField('e-mail', max_length=100,null=True,blank=True)
    telefono = models.IntegerField('Telefono', default=False, blank=False, null=False)
    fecha_nac = models.DateTimeField('Fecha de Nacimiento')
    sexo= models.ForeignKey(Sexo, on_delete=models.PROTECT)
    history = HistoricalRecords()

    def __str__(self):
        return self.nombre 