from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def Inicio(request):
     return render(request, 'inicio.html')
 
def Ingresos(request):
    return render(request, 'ingresos.html')

def Gastos(request):
    return render(request, 'gastos.html')

def Categorias(request):
    return render(request, 'categorias.html')

def IngresosFormulario(request):
    if request.method == 'POST':
        miFormulario = IngresosFormulario(request.POST) 
        print(miFormulario)
        if miFormulario.is_valid:
            inf = miFormulario.cleaned_data
            ingreso = Ingresos(descripcion=inf['descripcion'], monto=inf['monto'], fecha=inf['fecha'])
            ingreso.save()
            return render(request, 'inicio.html')
    else:
        miFormulario=Ingresosformulario()
        
    return render(request, 'ingresosFormulario.html', {'miFormulario': miFormulario})
