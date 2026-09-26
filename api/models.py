
from django.db import models


class Usuario(models.Model):

    ROLES = [
        ('adulto_mayor', 'Adulto Mayor'),
        ('voluntario', 'Voluntario'),
        ('administrador', 'Administrador'),
    ]

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    documento = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(unique=True)
    direccion = models.CharField(max_length=200)
    rol = models.CharField(max_length=30, choices=ROLES)
    activo = models.BooleanField(default=True)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Solicitud(models.Model):

    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('asignada', 'Asignada'),
        ('en_proceso', 'En proceso'),
        ('finalizada', 'Finalizada'),
        ('cancelada', 'Cancelada'),
    ]

    TIPOS = [
        ('compras', 'Compras'),
        ('diligencia', 'Diligencia'),
        ('acompanamiento', 'Acompañamiento'),
        ('comunitario', 'Apoyo comunitario'),
        ('otro', 'Otro'),
    ]

    adulto_mayor = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='solicitudes'
    )

    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=30, choices=TIPOS)
    direccion = models.CharField(max_length=200)

    estado = models.CharField(
        max_length=30,
        choices=ESTADOS,
        default='pendiente'
    )

    fecha_solicitud = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Asignacion(models.Model):

    solicitud = models.OneToOneField(
        Solicitud,
        on_delete=models.CASCADE,
        related_name='asignacion'
    )

    voluntario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='asignaciones'
    )

    fecha_asignacion = models.DateTimeField(auto_now_add=True)

    aceptada = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.voluntario} - {self.solicitud}"


class Actividad(models.Model):

    asignacion = models.OneToOneField(
        Asignacion,
        on_delete=models.CASCADE,
        related_name='actividad'
    )

    descripcion = models.TextField()

    fecha_realizacion = models.DateTimeField(
        auto_now_add=True
    )

    observaciones = models.TextField(
        blank=True,
        null=True
    )

    realizada = models.BooleanField(default=False)

    def __str__(self):
        return self.descripcion[:50]