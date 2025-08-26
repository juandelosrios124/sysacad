from django.db import models

class TipoDocumento(models.TextChoices):
    DNI = 'DNI', 'DNI'
    LIBRETA_CIVICA = 'LC', 'Libreta Cívica'
    LIBRETA_ENROLAMIENTO = 'LE', 'Libreta de Enrolamiento'
    PASAPORTE = 'PAS', 'Pasaporte'

    def __str__(self):
        return self.documentChoise


class User(models.Model):
    """
    Modelo que representa a un estudiante/maestro dentro del sistema académico.
    """
    SEXO_CHOICES = (
        ("M", "Masculino"),
        ("F", "Femenino"),
    )

    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    nroDocumento = models.CharField(max_length=20, unique=True)
    tipoDocumento = models.ForeignKey(TipoDocumento, on_delete=models.PROTECT)
    fechaNacimiento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    nroLegajo = models.PositiveIntegerField(unique=True)
    fechaIngreso = models.DateField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre} - Legajo: {self.nro_legajo}"

