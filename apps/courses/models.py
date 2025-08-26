# Create your models here.
from django.db import models
from apps.specialization.models import Materia, Plan
from apps.users.models import User


class Comision(models.Model):
    """
    Representa un grupo o comisión de estudiantes dentro de una materia/curso.
    """
    nombre = models.CharField(max_length=50)
    turno = models.CharField(max_length=20, choices=(("Mañana", "Mañana"), ("Tarde", "Tarde"), ("Noche", "Noche")), blank=True, null=True)

    def __str__(self):
        return f"Comision {self.nombre} ({self.turno})" if self.turno else f"Grupo {self.nombre}"


class Cursada(models.Model):
    """
    Representa la cursada de una materia en un cuatrimestre específico, 
    asignada a un grupo.
    """
    anio = models.PositiveIntegerField()
    cuatrimestre = models.PositiveSmallIntegerField(choices=((1, "Primer Cuatrimestre"), (2, "Segundo Cuatrimestre")))
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name="cursadas")
    grupo = models.ForeignKey(Comision, on_delete=models.SET_NULL, null=True, blank=True, related_name="cursadas")

    def __str__(self):
        return f"{self.materia.nombre} - {self.anio}/{self.cuatrimestre}"


class Correlatividad(models.Model):
    """
    Define una relación de correlatividad entre materias.
    Ejemplo: para cursar 'Algoritmos II' es necesario aprobar 'Algoritmos I'.
    """
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name="correlativas")
    correlativa = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name="requerida_por")

    def __str__(self):
        return f"{self.materia.nombre} requiere {self.correlativa.nombre}"


class Inscripcion(models.Model):
    """
    Inscripción de un alumno a una cursada.
    """
    alumno = models.ForeignKey(User, on_delete=models.CASCADE, related_name="inscripciones")
    cursada = models.ForeignKey(Cursada, on_delete=models.CASCADE, related_name="inscripciones")
    fecha_inscripcion = models.DateField(auto_now_add=True)
    estado = models.CharField(
        max_length=20,
        choices=(("Activa", "Activa"), ("Aprobada", "Aprobada"), ("Reprobada", "Reprobada"), ("Abandonada", "Abandonada")),
        default="Activa"
    )

    def __str__(self):
        return f"{self.alumno.apellido}, {self.alumno.nombre} - {self.cursada}"
