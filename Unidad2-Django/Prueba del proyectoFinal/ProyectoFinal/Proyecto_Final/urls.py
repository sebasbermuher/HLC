"""Proyecto_Final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Auth.views import auth
from Tareas.views import tareas
from Tareas.views import insertar_tareas, listar_tareas, mostrar_tarea, editar_tarea, borrar_tarea


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', auth),
    path('tareas/', tareas),
    path('insertar_tarea/', insertar_tareas),
    path('listar_tareas/', listar_tareas),
    path('mostrar_tarea/', mostrar_tarea),
    path('editar_tarea/<int:tarea_id>/', editar_tarea),
    path('borrar_tarea/<int:tarea_id>/', borrar_tarea),
]
