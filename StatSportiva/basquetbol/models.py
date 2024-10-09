from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Modelo Fase
class Fase(models.Model):
    """
    Representa una fase dentro de un campeonato. Cada fase está asociada a un campeonato y tiene un orden específico.
    """
    nombre = models.CharField(max_length=100)
    campeonato = models.ForeignKey('Campeonato', related_name='fases', on_delete=models.CASCADE)
    orden = models.PositiveIntegerField(help_text="Orden de la fase en el campeonato (1 para la fase inicial, etc.)")

    def __str__(self):
        return f"{self.nombre} - {self.campeonato.nombre}"


# Modelo Campeonato
class Campeonato(models.Model):
    """
    Representa un campeonato de baloncesto, con fechas de inicio y fin, descripción, límite de equipos y premios.
    """
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.TextField()
    max_equipos = models.PositiveIntegerField(default=10)
    premios = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nombre

    def equipo_count(self):
        """
        Retorna el número de equipos inscritos en el campeonato.
        """
        return self.equipos.count()

    def clean(self):
        """
        Valida que el número de equipos no exceda el máximo permitido.
        """
        if self.pk and self.equipo_count() > self.max_equipos:
            raise ValidationError(f'No se pueden inscribir más de {self.max_equipos} equipos en este campeonato.')


# Modelo Estadio
class Estadio(models.Model):
    """
    Representa un estadio donde se realizan los partidos, con nombre, capacidad y ciudad.
    """
    nombre = models.CharField(max_length=100)
    capacidad = models.PositiveIntegerField()
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


# Modelo Entrenador
class Entrenador(models.Model):
    """
    Representa a un entrenador asociado a un usuario, con nombre, nacionalidad y fecha de nacimiento.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre


# Modelo Jugador
class Jugador(models.Model):
    """
    Representa a un jugador en un equipo, con nombre, posición, número y equipo al que pertenece.
    """
    nombre = models.CharField(max_length=100)
    posicion = models.CharField(max_length=50)
    numero = models.PositiveIntegerField()
    equipo = models.ForeignKey('Equipo', related_name='jugadores', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.posicion} - {self.equipo.nombre}"


# Modelo Equipo
class Equipo(models.Model):
    """
    Representa un equipo en un campeonato, con un entrenador, fecha de fundación, historia, colores y logo.
    """
    nombre = models.CharField(max_length=100)
    campeonato = models.ForeignKey(Campeonato, related_name='equipos', on_delete=models.CASCADE)
    entrenador = models.OneToOneField(Entrenador, on_delete=models.CASCADE)
    fundacion = models.DateField()
    historia = models.TextField(null=True, blank=True)
    color_principal = models.CharField(max_length=7, help_text="Color principal en formato hexadecimal")
    color_secundario = models.CharField(max_length=7, help_text="Color secundario en formato hexadecimal")
    logo = models.ImageField(upload_to='logos_equipos/', null=True, blank=True)
    sitio_web = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nombre
