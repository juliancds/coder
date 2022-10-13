from django.http import HttpResponse
from django.shortcuts import render

from AppCoder.models import Profesor

# Create your views here.


def crear_profesor(request):
    profe = Profesor(nombre="ricardo", apellido="esposito", email="duki@gmail.com", profesion="abogado")
    
    profe.save()
    
    return HttpResponse(f"Estoy creando al profe: {profe.nombre} {profe.apellido}. su profesion es {profe.profesion}")