from django.contrib import admin
from gestion_pedidos.models import Articulos, Cliente, Pedidos

# Register your models here.


class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono')
    search_fields = ('nombre', 'direccion', 'telefono')
    list_filter = ('nombre', 'direccion', 'telefono')


class ArticulosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'seccion', 'precio')
    search_fields = ('nombre', 'seccion', 'precio')
    list_filter = ('nombre', 'seccion', 'precio')


class PedidosAdmin(admin.ModelAdmin):
    list_display = ('numero', 'fecha', 'entregado')
    search_fields = ('numero', 'fecha', 'entregado')
    list_filter = ('numero', 'fecha', 'entregado')


admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Cliente, ClientesAdmin)
admin.site.register(Pedidos, PedidosAdmin)
