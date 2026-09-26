from rest_framework.routers import DefaultRouter

from .views import (
    UsuarioViewSet,
    SolicitudViewSet,
    AsignacionViewSet,
    ActividadViewSet
)


router = DefaultRouter()

router.register(
    r'usuarios',
    UsuarioViewSet
)

router.register(
    r'solicitudes',
    SolicitudViewSet
)

router.register(
    r'asignaciones',
    AsignacionViewSet
)

router.register(
    r'actividades',
    ActividadViewSet
)


urlpatterns = router.urls