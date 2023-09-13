from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Inicio(request):
     return render(request, 'inicio.html')
 
def Ingresos(request):
    return render(request, 'ingresos.html')

def Gastos(request):
    return render(request, 'gastos.html')

def Categorias(request):
    return render(request, 'categorias.html')

def ingresosFormulario(request):
    if request.method == 'POST':
            ingresos =  Ingresos(request.post['descripcion'],(request.post['monto']))
            ingresos.save()
            return render(request, "inicio.html")
    return render(request, 'ingresosFormulario')
