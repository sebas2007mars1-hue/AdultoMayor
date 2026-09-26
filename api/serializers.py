from rest_framework import serializers
from .models import Usuario, Solicitud, Asignacion, Actividad


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = '__all__'


class SolicitudSerializer(serializers.ModelSerializer):

    class Meta:
        model = Solicitud
        fields = '__all__'


class AsignacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Asignacion
        fields = '__all__'


class ActividadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actividad
        fields = '__all__'