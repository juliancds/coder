from django.http import HttpResponse
from django.shortcuts import render

from AppCoder.models import Profesor

from AppCoder.models import Estudiante

# Create your views here.


def crear_profesor(request):
    profe = Profesor(nombre="ricardo", apellido="esposito", email="duki@gmail.com", profesion="abogado")
    
    profe.save()
    
    return HttpResponse(f"Estoy creando al profe: {profe.nombre} {profe.apellido}. su profesion es {profe.profesion}")

def mostrar_inicio(request):
    estudiante = Estudiante(nombre="Mauro", apellido="Lombardo", email="mauro@gmail.com")
    estudiante.save()
    contexto = {"estudiante_1": estudiante}
    return render(request, "AppCoder/inicio.html", contexto)