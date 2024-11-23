# utils.py
from .models import Partido, Posicion

def obtener_partidos(filtro=None):
    if filtro:
        return Partido.objects.filter(**filtro).order_by('fecha')
    return Partido.objects.all().order_by('fecha')

def obtener_posiciones(campeonato):
    return Posicion.objects.filter(campeonato=campeonato).order_by('-puntos', '-partidos_ganados')
