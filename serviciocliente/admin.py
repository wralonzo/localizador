from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter

from serviciocliente.models import ServicioCliente


# Funcion para exportar datos a formatos(excel, html, json)
# Permite genera un reporte de los datos seleccionados
class Exportar(resources.ModelResource):
    class Meta:
        model = ServicioCliente


@admin.register(ServicioCliente)
class ServicioClienteAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    # Campos a mostrar en la vista de bodequero
    # def queryset(self, request, queryset):
    #     qs = ServicioCliente.objects.filter(estado=True)
    #     return qs
    
    def get_queryset(self, request):
        if(request.GET.get('estado__exact', 0) == '0'):
            return ServicioCliente.objects.filter(estado=False)
        qs = ServicioCliente.objects.filter(estado=True)
        return qs.filter(estado=1)
    
    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_delete': False, # Here
            # 'show_save': False,
            'show_save_and_continue': False,
        })
        return super().render_change_form(request, context, add, change, form_url, obj)
    
    list_display = (
        "telefono", 
        "restaurante", 
        "pais", 
        "categoria", 
        "comentario",
        "usuario",
        "estado"
    )

    # Filtro que me permite generar reporte por fechas
    list_filter = ("pais", "estado","categoria", ("created_at", DateRangeFilter))

    # Funcion que me permite export a los diferentes formatos
    resource_class = Exportar

    # Encabezado el sitio
    date_hierarchy = "created_at"

    list_editable = [ "comentario", "usuario", "estado"]

    # Funcion que permite buscar por los atributos
    search_fields = ["telefono", "restaurante", "estado"]

    class Media:
        css = {
            'all': ('css/fancy.css',)
        }
    
    actions=['completar']
    
    def completar(self, request, queryset):
        queryset.update(estado=False)
        