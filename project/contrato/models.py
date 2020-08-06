from django.db import models
from simple_history.models import HistoricalRecords
from personas.models import Persona

class Estado(models.Model):
    id = models.AutoField(primary_key = True)
    estado = models.CharField('Estado ',blank=False,null=False,max_length=256)
    def __str__(self):
        return self.estado

class Objeto(models.Model):
    id = models.AutoField(primary_key = True)
    descripcion = models.CharField('Objeto ',blank=False,null=False,max_length=256)
    def __str__(self):
        return self.descripcion

class Solicitante(models.Model):
    id = models.AutoField(primary_key = True)
    solicitante = models.CharField('Solicitante ',blank=False,null=False,max_length=256)
    def __str__(self):
        return self.solicitante

class Contrato(models.Model):
    id = models.AutoField(primary_key = True)
    fecha_d=models.DateField()
    fecha_h=models.DateField()
    nro_dis=models.CharField('N Disponibilidad ',blank=False,null=False,max_length=8)
    estado=models.ForeignKey(Estado, on_delete=models.PROTECT)
    resumen=models.CharField('Resumen ',blank=False,null=False,max_length=250)
    nombre_archivo=models.CharField('Nombre de Archivo ',blank=False,null=False,max_length=50)
    fecha_c=models.DateField()
    anexo=models.CharField('Anexo ',blank=False,null=False,max_length=250)
    solicitante=models.ForeignKey(Solicitante, on_delete=models.PROTECT)
    persona=models.ForeignKey(Persona, on_delete=models.PROTECT)
    contrato=models.CharField('Contrato ',blank=False,null=False,max_length=10)
    objeto=models.ForeignKey(Objeto, on_delete=models.PROTECT)
    
