# basquetbol/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Partido, PartidoEstadistica, Campeonato, Campeon
from datetime import timedelta

@receiver(post_save, sender=PartidoEstadistica)
def avanzar_fase(sender, instance, **kwargs):
    """
    Avanza el torneo a la siguiente fase dependiendo de la fase actual.
    Primero avanza de cuartos a semifinales y luego de semifinales a final.
    Finalmente, declara al ganador de la final como campeón.
    """
    partido = instance.partido

    # Determinar la siguiente fase según la fase actual
    fases = {
        'Cuartos': 'Semifinal',
        'Semifinal': 'Final'
    }

    # Verificar si la fase actual está en el diccionario de fases
    if partido.fase in fases:
        nueva_fase = fases[partido.fase]
        campeonato = partido.campeonato

        # Verificar si ya existen los partidos de la siguiente fase
        if Partido.objects.filter(campeonato=campeonato, fase=nueva_fase).exists():
            print(f"Partidos de {nueva_fase} ya generados. No se generan nuevamente.")
            return

        # Verificar si todos los partidos de la fase actual tienen estadísticas registradas
        partidos_actuales = Partido.objects.filter(campeonato=campeonato, fase=partido.fase)
        if partidos_actuales.filter(estadisticas__isnull=True).exists():
            print(f"No todos los partidos de {partido.fase} tienen estadísticas registradas aún.")
            return

        # Obtener equipos ganadores de la fase actual
        equipos_ganadores = []
        for p in partidos_actuales:
            # Asegurarse de que las estadísticas existan para el partido
            if hasattr(p, 'estadisticas'):
                if p.estadisticas.puntos_equipo_local > p.estadisticas.puntos_equipo_visitante:
                    equipos_ganadores.append(p.equipo_local)
                elif p.estadisticas.puntos_equipo_visitante > p.estadisticas.puntos_equipo_local:
                    equipos_ganadores.append(p.equipo_visitante)
                else:
                    # Puedes decidir cómo manejar empates
                    equipos_ganadores.append(p.equipo_local)  # Ejemplo: elegir el equipo local en caso de empate
            else:
                print(f"El partido {p} no tiene estadísticas registradas.")
                return

        # Generar los partidos de la nueva fase
        if nueva_fase == 'Final' and len(equipos_ganadores) == 2:
            # Generar la final
            Partido.objects.create(
                campeonato=campeonato,
                equipo_local=equipos_ganadores[0],
                equipo_visitante=equipos_ganadores[1],
                fecha=partido.fecha + timedelta(days=7),
                estadio=partido.estadio,
                fase='Final'
            )
            print("Partido de la final creado exitosamente.")
        elif nueva_fase == 'Semifinal' and len(equipos_ganadores) == 4:
            # Generar las semifinales
            for i in range(0, len(equipos_ganadores), 2):
                Partido.objects.create(
                    campeonato=campeonato,
                    equipo_local=equipos_ganadores[i],
                    equipo_visitante=equipos_ganadores[i + 1],
                    fecha=partido.fecha + timedelta(days=7),
                    estadio=partido.estadio,
                    fase='Semifinal'
                )
            print("Partidos de semifinal creados exitosamente.")
        else:
            print(f"No hay suficientes equipos ganadores para crear los partidos de {nueva_fase}.")

    # Si la fase es "Final", determinar el campeón
    elif partido.fase == 'Final':
        campeonato = partido.campeonato
        if hasattr(partido, 'estadisticas'):
            if partido.estadisticas.puntos_equipo_local > partido.estadisticas.puntos_equipo_visitante:
                equipo_campeon = partido.equipo_local
            elif partido.estadisticas.puntos_equipo_visitante > partido.estadisticas.puntos_equipo_local:
                equipo_campeon = partido.equipo_visitante
            else:
                # Manejar el caso de empate en la final
                equipo_campeon = partido.equipo_local  # Ejemplo: elegir el equipo local en caso de empate

            # Verificar si ya existe un registro de campeón para este campeonato
            campeon, created = Campeon.objects.get_or_create(campeonato=campeonato, defaults={'equipo': equipo_campeon})
            if not created:
                # Si ya existe, actualizar al equipo campeón
                campeon.equipo = equipo_campeon
                campeon.save()

            print(f"¡El equipo {equipo_campeon.nombre_equipo} ha sido declarado campeón del campeonato {campeonato.nombre}!")

# signals.py

from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def enviar_correo_confirmacion(sender, instance, created, **kwargs):
    """
    Signal que se ejecuta cuando un usuario se crea. Envía un correo de confirmación.
    """
    if created:
        subject = 'Confirma tu correo electrónico'
        message = f'Hola {instance.username}, por favor confirma tu cuenta haciendo clic en el enlace.'
        recipient_list = [instance.email]
        
        # Enviar correo de confirmación
        send_mail(
            subject=subject, 
            message=message, 
            from_email='from@example.com', 
            recipient_list=recipient_list
        )
        print(f"Correo de confirmación enviado a {instance.email}")
