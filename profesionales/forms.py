
from django import forms

class CerrajeroFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    desempleado = forms.BooleanField(required=False) 
    


class CerrajeroBusqueda(forms.Form):
    nombre = forms.CharField(max_length=20)
    
    

class FutbolistaFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    club_futbol = forms.CharField(max_length=30) 



class IngenieroFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    especialidad = forms.CharField(max_length=150)
    desempleado = forms.BooleanField(required=False)  