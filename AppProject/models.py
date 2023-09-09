from django.db import models

# Create your models here.
   
class Ingresos(models.Model):
    descripcion= models.CharField(max_length=60)
    monto = models.FloatField()
    fecha = models.DateField(null=True, blank=True)
    
class Gastos(models.Model):
    descripcion = models.CharField(max_length=60)
    monto = models.FloatField()
    fecha = models.DateField(null=True, blank=True)

class Categorias(models.Model):
    nombre = models.CharField(max_length=40)
    