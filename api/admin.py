from django.contrib import admin
from .models import Usuario, Solicitud, Asignacion, Actividad


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'apellido',
        'rol',
        'telefono',
        'correo',
        'activo'
    )

    list_filter = ('rol', 'activo')
    search_fields = ('nombre', 'apellido', 'documento', 'correo')


@admin.register(Solicitud)
class SolicitudAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'adulto_mayor',
        'tipo',
        'estado',
        'fecha_solicitud'
    )

    list_filter = ('estado', 'tipo')
    search_fields = ('titulo', 'descripcion')


@admin.register(Asignacion)
class AsignacionAdmin(admin.ModelAdmin):
    list_display = (
        'solicitud',
        'voluntario',
        'aceptada',
        'fecha_asignacion'
    )

    list_filter = ('aceptada',)


@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = (
        'asignacion',
        'realizada',
        'fecha_realizacion'
    )

    list_filter = ('realizada',)