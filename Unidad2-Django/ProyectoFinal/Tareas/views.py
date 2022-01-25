from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.
def tareas(request):
    return HttpResponse("<h1>Esta es la pagina de Tareas</h1>")


def tareas(request):
    return render(request, "tareas.html")
