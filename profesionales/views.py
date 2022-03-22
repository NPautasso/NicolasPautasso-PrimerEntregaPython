from django.shortcuts import redirect, render
 
from .models import Cerrajero, Futbolista, Ingeniero
from .forms import CerrajeroFormulario, CerrajeroBusqueda, FutbolistaFormulario, IngenieroFormulario

# Create your views here.


def crear_cerrajero(request):
    
    if request.method == 'POST':
        form = CerrajeroFormulario(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            cerrajero = Cerrajero(nombre=data['nombre'], apellido=data['apellido'], desempleado=data['desempleado'])
            cerrajero.save()
            # return render(request, "index/index.html", {})
            return redirect('index')
     
    form = CerrajeroFormulario()
    return render(request,"profesionales/crear_cerrajero.html", {'form': form})


def lista_cerrajeros(request):
    
    
    nombre_a_buscar = request.GET.get('nombre', None)
    
    
    if nombre_a_buscar is not None:
        cerrajeros = Cerrajero.objects.filter(nombre__icontains=nombre_a_buscar)
    else:
        cerrajeros = Cerrajero.objects.all()
        
        
    # cerrajeros = None
    form = CerrajeroBusqueda()
    return render(request,"profesionales/lista_cerrajeros.html", {'form': form, 'cerrajeros': cerrajeros})



def crear_futbolista(request):
    
    if request.method == 'POST':
        form = FutbolistaFormulario(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            futbolista = Futbolista(nombre=data['nombre'], apellido=data['apellido'], club_futbol=data['club_futbol'])
            futbolista.save()
            # return render(request, "index/index.html", {})
            return redirect('index')
     
    form = FutbolistaFormulario()
    return render(request,"profesionales/crear_futbolista.html", {'form': form})

def crear_ingeniero(request):
    
    if request.method == 'POST':
        form = IngenieroFormulario(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            ingeniero = Ingeniero(nombre=data['nombre'], apellido=data['apellido'], especialidad=data['especialidad'], desempleado=data['desempleado'])
            ingeniero.save()
            # return render(request, "index/index.html", {})
            return redirect('index')
     
    form = IngenieroFormulario()
    return render(request,"profesionales/crear_ingeniero.html", {'form': form})