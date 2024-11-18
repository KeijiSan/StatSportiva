from django.contrib import admin

from .models import Fase, Campeonato, Estadio, Entrenador, Jugador, Equipo, Video

# Registrar los modelos para que puedan ser gestionados desde el administrador de Django
admin.site.register(Fase)
admin.site.register(Campeonato)
admin.site.register(Estadio)
admin.site.register(Entrenador)
admin.site.register(Jugador)
admin.site.register(Equipo)
admin.site.register(Video)  # Registrar el modelo Video

# Register your models here.
