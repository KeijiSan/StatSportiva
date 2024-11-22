from django.contrib import admin

from .models import Fase, Campeonato, Estadio, Entrenador, Jugador, Equipo, Video

# Register your models here.
admin.site.register(Video)  # Registrar el modelo Video
