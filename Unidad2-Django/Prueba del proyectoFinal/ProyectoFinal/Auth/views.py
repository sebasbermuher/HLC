from django.shortcuts import render
from django.http.response import HttpResponse
import datetime


# Create your views here.
def auth(request):
    return HttpResponse("<h1>Esta es la pagina de Auth</h1>")


# class Persona(object):
#     def __init__(self, nombre, apellido):
#         self.nombre = nombre
#         self.apellido = apellido


# def auth(request):
#     persona = Persona("Sebastian", "Bermudez")
#     temas_del_curso = ["Formularios", "Modelos", "Vistas", "Despliegue"]
#     fecha_actual = datetime.datetime.now()
#     return render(request, "login.html", {"nombre_persona": persona.nombre, "apellido_persona": persona.apellido, "fecha_actual": fecha_actual, "temas": temas_del_curso})

def auth(request):
    return render(request, "login.html")
