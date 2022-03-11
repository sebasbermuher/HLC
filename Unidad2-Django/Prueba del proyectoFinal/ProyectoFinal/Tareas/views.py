from django.shortcuts import render
from django.http.response import HttpResponse
from Tareas.models import Tarea
from datetime import datetime


# Create your views here.
def tareas(request):
    return HttpResponse("<h1>Esta es la pagina de Tareas</h1>")


def tareas(request):
    return render(request, "tareas.html")


# def mostrar_tareas(request):
#     if (request.method == 'POST'):
#         tarea = Tareas()
#         tarea.fecha = request.POST["fecha"]
#         tarea.horas = request.POST["horas"]
#         tarea.descripcion = request.POST["descripcion"]
#         tarea.save()
#         return render(request, 'mostrar_tareas.html', {'tarea': tarea})
#     else:
#         return render(request, 'mostrar_tareas.html', {'tarea': None})


def insertar_tareas(request):
    if (request.method == 'POST' and request.user.id != None):
        tarea = Tarea()
        tarea.user_id = request.user.id
        tarea.fecha = request.POST["fecha"]
        tarea.horas = request.POST["horas"]
        tarea.descripcion = request.POST["descripcion"]
        tarea.save()
        return render(request, 'mostrar_tarea.html', {'tarea': tarea})
    else:
        tarea = Tarea()
        tarea.user_id = request.user.id
        tarea.fecha = datetime.now()
        tarea.horas = 0
        tarea.descripcion = ""
        return render(request, 'insertar_tareas.html', {'tarea': tarea, 'action': '/insertar_tarea/'})


def listar_tareas(request):
    tareas = Tarea.objects.filter(user_id=request.user.id)
    return render(request, 'listar_tareas.html', {'tareas': tareas})


def mostrar_tarea(request):
    if (request.method == 'POST' and request.user.id != None):
        tarea = Tarea.objects.get(id=request.POST["id"])
        return render(request, 'mostrar_tarea.html', {'tarea': tarea})


def editar_tarea(request, tarea_id):
    if (request.method == 'POST' and request.user.id != None):
        tarea = Tarea.objects.get(id=tarea_id)
        tarea.fecha = request.POST["fecha"]
        tarea.horas = request.POST["horas"]
        tarea.descripcion = request.POST["descripcion"]
        tarea.save()
        print("salvando tarea editada")
        print(tarea)
        return render(request, 'mostrar_tarea.html', {'tarea': tarea})
    else:
        print("editando tarea")
        tarea = Tarea.objects.get(id=tarea_id)
        return render(request, 'insertar_tareas.html', {'tarea': tarea, 'action': '/editar_tarea/{}/'.format(tarea_id)})


def borrar_tarea(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.delete()
    return render(request, 'borrar_tarea.html', {'tarea': tarea})
