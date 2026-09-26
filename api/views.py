from rest_framework import viewsets

from .models import (
    Usuario,
    Solicitud,
    Asignacion,
    Actividad
)

from .serializers import (
    UsuarioSerializer,
    SolicitudSerializer,
    AsignacionSerializer,
    ActividadSerializer
)


class UsuarioViewSet(viewsets.ModelViewSet):

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class SolicitudViewSet(viewsets.ModelViewSet):

    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer


class AsignacionViewSet(viewsets.ModelViewSet):

    queryset = Asignacion.objects.all()
    serializer_class = AsignacionSerializer


class ActividadViewSet(viewsets.ModelViewSet):

    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer