from django.db import models

# Create your models here.
from django.db import models
class Orientacion(models.Model):
    """
    Representa una orientación académica dentro de una especialidad.
    """
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


class TipoEspecialidad(models.Model):
    """
    Clasificación de la especialidad (ejemplo: Técnica, Licenciatura, etc.)
    """
    nombre = models.CharField(max_length=100)
    nivel = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} - Nivel: {self.nivel}"


class Especialidad(models.Model):
    """
    Representa una especialidad dentro de la facultad.
    """
    nombre = models.CharField(max_length=150)
    letra = models.CharField(max_length=5, blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)

    # Relaciones
    tipo = models.ForeignKey(TipoEspecialidad, on_delete=models.SET_NULL, null=True, blank=True, related_name="especialidades")
    orientaciones = models.ManyToManyField(Orientacion, related_name="especialidades", blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.letra})" if self.letra else self.nombre


class Plan(models.Model):
    """
    Plan de estudios asociado a una especialidad.
    """
    nombre = models.CharField(max_length=150)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)

    # Relaciones
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, related_name="planes")

    def __str__(self):
        return f"Plan {self.nombre} - {self.especialidad.nombre}"


class Materia(models.Model):
    """
    Materias o asignaturas que pertenecen a un plan de estudios.
    """
    nombre = models.CharField(max_length=150)
    codigo = models.CharField(max_length=20, unique=True)
    observacion = models.TextField(blank=True, null=True)

    # Relaciones
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name="materias")

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"
