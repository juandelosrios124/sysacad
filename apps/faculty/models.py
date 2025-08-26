from django.db import models

from django.db import models


class Universidad(models.Model):
    """
    Representa la universidad a la cual pertenece una facultad.
    """
    nombre = models.CharField(max_length=150)
    sigla = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.nombre} ({self.sigla})"


class Departamento(models.Model):
    """
    Departamentos académicos dentro de una facultad.
    """
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Orientacion(models.Model):
    """
    Orientaciones académicas disponibles en una facultad.
    """
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Especialidad(models.Model):
    """
    Especialidades académicas que puede ofrecer una facultad.
    """
    nombre = models.CharField(max_length=100)
    letra = models.CharField(max_length=5, blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Facultad(models.Model):
    """
    Representa una facultad dentro de una universidad.
    """

    nombre = models.CharField(max_length=150)
    abreviatura = models.CharField(max_length=20, blank=True, null=True)
    directorio = models.CharField(max_length=150, blank=True, null=True)
    sigla = models.CharField(max_length=20, blank=True, null=True)
    codigo_postal = models.CharField(max_length=10, blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    domicilio = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    contacto = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    # Relaciones
    universidad = models.ForeignKey(Universidad, on_delete=models.CASCADE, related_name="facultades")
    departamentos = models.ManyToManyField(Departamento, related_name="facultades", blank=True)
    orientaciones = models.ManyToManyField(Orientacion, related_name="facultades", blank=True)
    especialidades = models.ManyToManyField(Especialidad, related_name="facultades", blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.sigla})" if self.sigla else self.nombre
