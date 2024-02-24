from django.contrib import admin

# Register your models here.
from .models import Categoria,Autor
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class AutorResource(resources.ModelResource):
    class Meta:
        model=Autor

    def __str__(self):
        pass
class CategoriaResource(resources.ModelResource):
    class Meta:
        model=Categoria

    def __str__(self):
        pass
class AutorAdmin(ImportExportModelAdmin,admin.ModelAdmin):

    search_fields=['nombre','apellidos','correo']
    list_display=('nombre','apellidos','correo','estado','fecha_creacion',)
    resource_class=AutorResource

class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):

    search_fields=['nombre']
    list_display=('nombre','estado','fecha_creacion',)
    resource_class=CategoriaResource


admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Autor,AutorAdmin)
# admin.site.register(Categoria)
# admin.site.register(Autor)

