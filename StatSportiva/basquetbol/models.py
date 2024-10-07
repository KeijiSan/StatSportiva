from django.db import models
from django.core.exceptions import ValidationError

# Modelo Fase
class Fase(models.Model):
    nombre = models.CharField(max_length=100)
    campeonato = models.ForeignKey('Campeonato', related_name='fases', on_delete=models.CASCADE)
    orden = models.PositiveIntegerField(help_text="Orden de la fase en el campeonato (1 para la fase inicial, etc.)")

    def __str__(self):
        return f"{self.nombre} - {self.campeonato.nombre}"

# Modelo Campeonato
class Campeonato(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.TextField()
    max_equipos = models.PositiveIntegerField(default=10)
    premios = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nombre

    def equipo_count(self):
        # Contamos el número de equipos asociados a este campeonato
        return self.equipos.count()

    def clean(self):
        # Validación para evitar que se inscriban más equipos de los permitidos
        if self.pk and self.equipo_count() > self.max_equipos:
            raise ValidationError(f'No se pueden inscribir más de {self.max_equipos} equipos en este campeonato.')

# Modelo Estadio
class Estadio(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.PositiveIntegerField()
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Modelo Entrenador
from django.contrib.auth.models import User
from django.db import models

class Entrenador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre



# Modelo Jugador
class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    posicion = models.CharField(max_length=50)
    numero = models.PositiveIntegerField()
    equipo = models.ForeignKey('Equipo', related_name='jugadores', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.posicion} - {self.equipo.nombre}"

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    campeonato = models.ForeignKey(Campeonato, related_name='equipos', on_delete=models.CASCADE)
    entrenador = models.OneToOneField(Entrenador, on_delete=models.CASCADE)  # Relación con entrenador
    fundacion = models.DateField()
    historia = models.TextField(null=True, blank=True)
    color_principal = models.CharField(max_length=7, help_text="Color principal en formato hexadecimal")
    color_secundario = models.CharField(max_length=7, help_text="Color secundario en formato hexadecimal")
    logo = models.ImageField(upload_to='logos_equipos/', null=True, blank=True)
    sitio_web = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nombre  # Asegúrate de mostrar solo el nombre del equipo
