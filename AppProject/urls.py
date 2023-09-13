from django.urls import path
from .views import *

urlpatterns = [
    path('', Inicio, name='Inicio'),
    path('Ingresos/', Ingresos, name='Ingresos'),
    path('Gastos/', Gastos, name='Gastos'),
    path('Categorias/', Categorias, name='Categorias'),
    path('IngresosFomulario/', ingresosFormulario name='IngresosFormulario'),
]