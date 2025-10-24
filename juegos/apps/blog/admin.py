from django.contrib import admin
from .models import Categoria, Articulo, ImagenArticulo

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

# Inline para cargar varias imágenes dentro de un Articulo
class ImagenArticuloInline(admin.TabularInline):  # o admin.StackedInline si prefieres formato vertical
    model = ImagenArticulo
    extra = 1  # cantidad de formularios vacíos que aparecen por defecto

class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'categoria', 'fecha_publicacion', 'destacado', 'visitas')
    list_filter = ('categoria', 'destacado')
    search_fields = ('titulo', 'contenido')
    inlines = [ImagenArticuloInline]  # 👈 permite cargar imágenes en el mismo formulario del artículo

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Articulo, ArticuloAdmin)