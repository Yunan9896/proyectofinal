from django.db import models

# Create your models here.
   
class Ingresos(models.Model):
    descripcion= models.CharField(max_length=60)
    monto = models.FloatField()
    fecha = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.descripcion} - {self.monto}'
    
class Gastos(models.Model):
    descripcion = models.CharField(max_length=60)
    monto = models.FloatField()
    fecha = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.descripcion} - {self.monto}'

class Categorias(models.Model):
    nombre = models.CharField(max_length=40)
    
    def __str__(self):
        return f'{self.descripcion}'