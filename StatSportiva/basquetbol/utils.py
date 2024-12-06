# utils.py
from .models import Partido, Posicion

def obtener_partidos(filtro=None):
    if filtro:
        return Partido.objects.filter(**filtro).order_by('fecha')
    return Partido.objects.all().order_by('fecha')

def obtener_posiciones(campeonato):
    return Posicion.objects.filter(campeonato=campeonato).order_by('-puntos', '-partidos_ganados')

# basquetbol/utils.py
import joblib
import pandas as pd
from django.db.models import Avg
from basquetbol.models import PartidoEstadistica

def calcular_probabilidades_sin_estadisticas(partido):
    model = joblib.load('modelo_prediccion_partidos.pkl')
    
    equipo_local = partido.equipo_local
    equipo_visitante = partido.equipo_visitante

    # Calcular promedios de partidos anteriores
    promedios_local = PartidoEstadistica.objects.filter(partido__equipo_local=equipo_local).aggregate(
        avg_pases=Avg('pases_equipo_local'),
        avg_faltas=Avg('faltas_equipo_local'),
        avg_triples=Avg('triples_equipo_local'),
        avg_rebotes=Avg('rebotes_equipo_local'),
        avg_puntos=Avg('puntos_equipo_local')
    )

    promedios_visitante = PartidoEstadistica.objects.filter(partido__equipo_visitante=equipo_visitante).aggregate(
        avg_pases=Avg('pases_equipo_visitante'),
        avg_faltas=Avg('faltas_equipo_visitante'),
        avg_triples=Avg('triples_equipo_visitante'),
        avg_rebotes=Avg('rebotes_equipo_visitante'),
        avg_puntos=Avg('puntos_equipo_visitante')
    )

    data = {
        'prom_pases_equipo_local': [promedios_local['avg_pases'] or 0],
        'prom_faltas_equipo_local': [promedios_local['avg_faltas'] or 0],
        'prom_triples_equipo_local': [promedios_local['avg_triples'] or 0],
        'prom_rebotes_equipo_local': [promedios_local['avg_rebotes'] or 0],
        'prom_puntos_equipo_local': [promedios_local['avg_puntos'] or 0],
        'prom_pases_equipo_visitante': [promedios_visitante['avg_pases'] or 0],
        'prom_faltas_equipo_visitante': [promedios_visitante['avg_faltas'] or 0],
        'prom_triples_equipo_visitante': [promedios_visitante['avg_triples'] or 0],
        'prom_rebotes_equipo_visitante': [promedios_visitante['avg_rebotes'] or 0],
        'prom_puntos_equipo_visitante': [promedios_visitante['avg_puntos'] or 0],
    }

    df = pd.DataFrame(data)
    prediccion = model.predict_proba(df)

    return round(prediccion[0][1] * 100, 2), round(prediccion[0][0] * 100, 2)


from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from django.utils.encoding import force_bytes

def send_confirmation_email(user, request):
    """Envía un correo de confirmación al usuario recién registrado."""
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))  # Codificar el ID del usuario
    current_site = request.get_host()

    activation_link = f"{request.scheme}://{current_site}/confirmar/{uid}/{token}/"
    subject = 'Confirmación de Registro'
    message = (
        f"Hola {user.username},\n\n"
        f"Gracias por registrarte en nuestra plataforma. Por favor, confirma tu cuenta "
        f"haciendo clic en el siguiente enlace:\n\n{activation_link}\n\n"
        "Si no solicitaste esta cuenta, ignora este mensaje.\n\nSaludos,\nEquipo de Soporte."
    )
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])