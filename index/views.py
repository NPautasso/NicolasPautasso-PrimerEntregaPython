from json import load
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index/index.html', {})

def plantilla(request):
    
    datos = {
        'lista': ['primero', 'segundo', 'tercero'],
        'nombre': 'Juancho'
    }
    
    return render(request, 'index/plantilla.html', datos)