from django.shortcuts import render
from gestion_pedidos.models import Articulos
from gestion_pedidos.forms import FormularioContacto


# Create your views here.

from django.http import HttpResponse


def busqueda_productos(request):
    return render(request, 'busqueda_producto.html')


# def contacto(request):
#     return render(request, 'contacto.html')

def contacto(request):

    if request.method == 'POST':
        return render(request, 'gracias.html', {'data': request.POST})

    return render(request, 'contacto.html')

# def buscar(request):
#     mensaje = "Articulo buscado: {}".format(request.GET['prd'])
#     return HttpResponse(mensaje)


def buscar(request):
    if request.GET['prd']:
        producto = request.GET['prd']
        if len(producto) > 20:
            return HttpResponse("El producto no puede tener mas de 20 caracteres")
        else:
            articulos = Articulos.objects.filter(nombre__icontains=producto)
            return render(request, 'resultados_busqueda.html', {'articulos': articulos, 'query': producto})
    else:
        mensaje = "No se ha introducido ningun producto"
    return HttpResponse(mensaje)


def api_contacto(request):
    if request.method == 'POST':
        form = FormularioContacto(request.POST)
        if form.is_valid():
            return render(request, 'gracias.html', {'data': form.cleaned_data})
    else:
        form = FormularioContacto()
        return render(request, 'api_contacto.html', {'form': form})
