from django.contrib import admin

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre", "direccion", "tfno") #Se visualizan los tres campos en la presentación de cada registro
    search_fields=("nombre", "tfno") #Agrega Búsqueda por nombre y teléfono en este caso en la plantilla Administración
    
class ArticulosAdmin(admin.ModelAdmin):
    list_filter=("nombre", "seccion",) #Agregamos filtro por sección /Es una tupla por eso termina en ,
    
class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero", "fecha")
    list_filter=("fecha",)
    date_hierarchy="fecha" #Filtros Superiores

from gestionPedidos.models import Clientes, Articulos, Pedidos
admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)




