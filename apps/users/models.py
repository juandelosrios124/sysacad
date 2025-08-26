from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class TipoDocumento(models.Model):
    """
    Tipos de documentos válidos para los usuarios (DNI, Pasaporte, etc.)
    """
    tipoDocumento = (
        ("DNI", "Documento Nacional de Identidad"),
        ("LC", "Libreta Cívica"),
        ("Le", "Libreta de Enrolamiento"),
        ("PAS", "Pasaporte"),
    )

    def __str__(self):
        return self.tipoDocumento

class CustomUser(AbstractUser):
    """
    Usuario base del sistema. 
    Extiende el usuario de Django para almacenar datos personales comunes.
    """

    SEXO_CHOICES = (
        ("M", "Masculino"),
        ("F", "Femenino"),
        ("O", "Otro"),
    )

    # Datos personales
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.PROTECT, null=True, blank=True)
    nro_documento = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=True, blank=True)

    # Datos institucionales (si aplica)
    nro_legajo = models.PositiveIntegerField(unique=True, null=True, blank=True)
    fecha_ingreso = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre} ({self.username})"


class Alumno(models.Model):
    """
    Perfil específico de Alumno. 
    Relación 1 a 1 con CustomUser.
    """
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="alumno")

    # Campos propios de alumnos
    promedio_general = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    plan_estudio = models.ForeignKey(
        "specialization.Plan", on_delete=models.SET_NULL, null=True, blank=True, related_name="alumnos"
    )

    def __str__(self):
        return f"Alumno {self.usuario.apellido}, {self.usuario.nombre}"


class Profesor(models.Model):
    """
    Perfil específico de Profesor.
    Relación 1 a 1 con CustomUser.
    """
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="profesor")

    # Campos propios de profesores
    titulo = models.CharField(max_length=150, blank=True, null=True)
    especialidad = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Profesor {self.usuario.apellido}, {self.usuario.nombre}"


class Administrativo(models.Model):
    """
    Perfil específico de Personal Administrativo.
    Relación 1 a 1 con CustomUser.
    """
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="administrativo")

    # Campos propios de administrativos
    area = models.CharField(max_length=100, blank=True, null=True)
    cargo = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Administrativo {self.usuario.apellido}, {self.usuario.nombre}"
    
