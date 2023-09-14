from django import forms
 
class Ingresosformulario(forms.Form):
    descripcion = forms.CharField()
    monto = forms.FloatField()
    fecha = forms.DateTimeField()
