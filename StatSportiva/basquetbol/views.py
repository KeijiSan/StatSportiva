
#-------------------------- IMPORTS --------------------------
from django.utils.encoding import force_bytes
import joblib
from django.utils.http import urlsafe_base64_encode
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth import login as auth_login
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.http import JsonResponse
from django.db.models import F, Q, Sum
from django.utils.timezone import now
from itertools import combinations
from random import shuffle, choice
from datetime import timedelta
import joblib
import pandas as pd

from .forms import (
    ComentarioForm, InscripcionEquipoForm, EntrenadorForm, JugadorFormSet, CrearCampeonatoForm, PublicacionForm, RegistroForm, PartidoStatsForm
)

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .models import Campeon, Campeonato, Entrenador, Equipo, Estadio, Jugador, PartidoEstadistica, Publicacion, Video  # Importa el modelo Video

#---------------------------------------------- FIN IMPORTS --------------------------------------------------





#------------------------- keiji ------------------------------------------------------------------------

from django.shortcuts import render, get_object_or_404, redirect




from django.urls import reverse

# Vista para la Política de Privacidad
def politica_privacidad(request):
    return render(request, 'basquetbol/politica_privacidad.html')

from django.shortcuts import render
from .models import Posicion  # Modelo que contiene la tabla de posiciones
from django.db.models import Avg

def tabla_posiciones(request):
    posiciones = Posicion.objects.all().order_by('-puntos', '-partidos_ganados')  # Ordenar por puntos y partidos ganados
    return render(request, 'basquetbol/tabla_posiciones.html', {'posiciones': posiciones})



def nosotros(request):
    return render(request, 'basquetbol/sobre_nosotros.html')




#---------------------------------------- Pagina principal, USUARIO ----------------------------------------------------------------

from .models import Partido

from django.shortcuts import render
from .models import Partido

from django.db.models import Avg
from django.utils.timezone import now
import joblib
import pandas as pd
from basquetbol.models import Partido
from django.shortcuts import render
from django.utils.timezone import now
from .models import Partido
from django.shortcuts import render
from django.utils.timezone import now
import pandas as pd
from basquetbol.models import Partido

from django.shortcuts import render
from django.utils.timezone import now
import joblib
import pandas as pd
from .models import Partido
import sklearn.externals




def partidos_con_estadisticas(request):
    """
    Retorna todos los partidos que tienen estadísticas registradas.
    """
    partidos = Partido.objects.filter(estadisticas__isnull=False).order_by('fecha')  # Filtrar partidos con estadísticas
    return render(request, 'basquetbol/proximo_partido.html', {'partidos': partidos})

import os

def proximo_partido(request):
    equipo_inscrito = (
        Equipo.objects.filter(entrenador__user=request.user).exists()
        if request.user.is_authenticated
        else False
    )
    """
    Muestra el próximo partido y calcula las probabilidades si aplica.
    Responde a solicitudes AJAX con datos del próximo partido.
    """
    # Manejo de solicitudes AJAX
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        partido = Partido.objects.filter(fecha__gte=now()).order_by('fecha').first()
        if partido:
            estadisticas = getattr(partido, 'estadisticas', None)
            data = {
                'equipo_local': partido.equipo_local.nombre_equipo,
                'equipo_visitante': partido.equipo_visitante.nombre_equipo,
                'puntos_local': estadisticas.puntos_equipo_local if estadisticas else 0,
                'puntos_visitante': estadisticas.puntos_equipo_visitante if estadisticas else 0,
                'fecha': partido.fecha,
                'estadio': partido.estadio.nombre if partido.estadio else "No disponible",
            }
            return JsonResponse(data)
        return JsonResponse({'error': 'No hay próximo partido programado'}, status=404)

    # Solicitudes normales
    proximo_partido = Partido.objects.filter(fecha__gte=now()).order_by('fecha').first()
    partidos_con_estadisticas = Partido.objects.filter(estadisticas__isnull=False).order_by('fecha')
    probabilidad_local = "No disponible"
    probabilidad_visitante = "No disponible"

    # Calcular probabilidades si hay un próximo partido
    if proximo_partido:
        try:
            model_path = os.path.join('media', 'modelos', 'modelo_prediccion_partidos_avanzado.pkl')
            model = joblib.load(model_path)

            if hasattr(proximo_partido, 'estadisticas') and proximo_partido.estadisticas:
                estadisticas = proximo_partido.estadisticas
                data = {
                    'pases_equipo_local': [estadisticas.pases_equipo_local],
                    'faltas_equipo_local': [estadisticas.faltas_equipo_local],
                    'triples_equipo_local': [estadisticas.triples_equipo_local],
                    'rebotes_ofensivos_local': [estadisticas.rebotes_ofensivos_equipo_local],
                    'rebotes_defensivos_local': [estadisticas.rebotes_defensivos_equipo_local],
                    'robos_equipo_local': [estadisticas.robos_equipo_local],
                    'puntos_equipo_local': [estadisticas.puntos_equipo_local],
                    'pases_equipo_visitante': [estadisticas.pases_equipo_visitante],
                    'faltas_equipo_visitante': [estadisticas.faltas_equipo_visitante],
                    'triples_equipo_visitante': [estadisticas.triples_equipo_visitante],
                    'rebotes_ofensivos_visitante': [estadisticas.rebotes_ofensivos_equipo_visitante],
                    'rebotes_defensivos_visitante': [estadisticas.rebotes_defensivos_equipo_visitante],
                    'robos_equipo_visitante': [estadisticas.robos_equipo_visitante],
                    'puntos_equipo_visitante': [estadisticas.puntos_equipo_visitante],
                }
            else:
                equipo_local = proximo_partido.equipo_local
                equipo_visitante = proximo_partido.equipo_visitante

                # Obtener estadísticas promedio para equipos
                estadisticas_local = PartidoEstadistica.objects.filter(partido__equipo_local=equipo_local).aggregate(
                    pases_equipo_local=Avg('pases_equipo_local'),
                    faltas_equipo_local=Avg('faltas_equipo_local'),
                    triples_equipo_local=Avg('triples_equipo_local'),
                    rebotes_ofensivos_local=Avg('rebotes_ofensivos_equipo_local'),
                    rebotes_defensivos_local=Avg('rebotes_defensivos_equipo_local'),
                    robos_equipo_local=Avg('robos_equipo_local'),
                    puntos_equipo_local=Avg('puntos_equipo_local'),
                )

                estadisticas_visitante = PartidoEstadistica.objects.filter(partido__equipo_visitante=equipo_visitante).aggregate(
                    pases_equipo_visitante=Avg('pases_equipo_visitante'),
                    faltas_equipo_visitante=Avg('faltas_equipo_visitante'),
                    triples_equipo_visitante=Avg('triples_equipo_visitante'),
                    rebotes_ofensivos_visitante=Avg('rebotes_ofensivos_equipo_visitante'),
                    rebotes_defensivos_visitante=Avg('rebotes_defensivos_equipo_visitante'),
                    robos_equipo_visitante=Avg('robos_equipo_visitante'),
                    puntos_equipo_visitante=Avg('puntos_equipo_visitante'),
                )

                data = {
                    'pases_equipo_local': [estadisticas_local['pases_equipo_local'] or 0],
                    'faltas_equipo_local': [estadisticas_local['faltas_equipo_local'] or 0],
                    'triples_equipo_local': [estadisticas_local['triples_equipo_local'] or 0],
                    'rebotes_ofensivos_local': [estadisticas_local['rebotes_ofensivos_local'] or 0],
                    'rebotes_defensivos_local': [estadisticas_local['rebotes_defensivos_local'] or 0],
                    'robos_equipo_local': [estadisticas_local['robos_equipo_local'] or 0],
                    'puntos_equipo_local': [estadisticas_local['puntos_equipo_local'] or 0],
                    'pases_equipo_visitante': [estadisticas_visitante['pases_equipo_visitante'] or 0],
                    'faltas_equipo_visitante': [estadisticas_visitante['faltas_equipo_visitante'] or 0],
                    'triples_equipo_visitante': [estadisticas_visitante['triples_equipo_visitante'] or 0],
                    'rebotes_ofensivos_visitante': [estadisticas_visitante['rebotes_ofensivos_visitante'] or 0],
                    'rebotes_defensivos_visitante': [estadisticas_visitante['rebotes_defensivos_visitante'] or 0],
                    'robos_equipo_visitante': [estadisticas_visitante['robos_equipo_visitante'] or 0],
                    'puntos_equipo_visitante': [estadisticas_visitante['puntos_equipo_visitante'] or 0],
                }

            df = pd.DataFrame(data)
            prediccion = model.predict_proba(df)

            probabilidad_local = round(prediccion[0][1] * 100, 2)
            probabilidad_visitante = round(prediccion[0][0] * 100, 2)

        except Exception as e:
            print(f"Error al calcular probabilidades: {e}")

    # Obtener posiciones y videos
    posiciones = Posicion.objects.all().order_by('-puntos')
    videos = Video.objects.all()

    # Ajustar URLs de videos
    for video in videos:
        if "shorts" in video.url:
            video_id = video.url.split('/')[-1]
            video.url = f"https://www.youtube.com/embed/{video_id}"

    return render(
        request,
        'basquetbol/proximo_partido.html',
        {
            'proximo_partido': proximo_partido,
            'partidos_con_estadisticas': partidos_con_estadisticas,
            'probabilidad_local': probabilidad_local,
            'probabilidad_visitante': probabilidad_visitante,
            'posiciones': posiciones,
            'videos': videos,
            'equipo_inscrito': equipo_inscrito,
        },
    )

import pandas as pd
from django.shortcuts import render
from django.utils.timezone import now
from .models import Partido, Equipo, Posicion, Video

def proximo_partido_con_estadisticas(request):
    # Verificar si el usuario tiene un equipo inscrito
    equipo_inscrito = (
        Equipo.objects.filter(entrenador__user=request.user).exists()
        if request.user.is_authenticated
        else False
    )

    # Obtener el partido más cercano con estadísticas registradas
    partido_con_estadisticas = (
        Partido.objects.filter(fecha__gte=now(), estadisticas__isnull=False)
        .order_by('fecha')
        .first()
    )

    probabilidad_local = None
    probabilidad_visitante = None

    if partido_con_estadisticas and hasattr(partido_con_estadisticas, 'estadisticas'):
        try:
            # Cargar el modelo de predicción
            model = joblib.load('modelo_prediccion_partidos.pkl')

            # Preparar los datos para el modelo
            estadisticas = partido_con_estadisticas.estadisticas
            data = {
                'pases_equipo_local': [estadisticas.pases_equipo_local],
                'faltas_equipo_local': [estadisticas.faltas_equipo_local],
                'triples_equipo_local': [estadisticas.triples_equipo_local],
                'rebotes_equipo_local': [estadisticas.rebotes_equipo_local],
                'puntos_equipo_local': [estadisticas.puntos_equipo_local],
                'pases_equipo_visitante': [estadisticas.pases_equipo_visitante],
                'faltas_equipo_visitante': [estadisticas.faltas_equipo_visitante],
                'triples_equipo_visitante': [estadisticas.triples_equipo_visitante],
                'rebotes_equipo_visitante': [estadisticas.rebotes_equipo_visitante],
                'puntos_equipo_visitante': [estadisticas.puntos_equipo_visitante],
            }

            df = pd.DataFrame(data)
            prediccion = model.predict_proba(df)

            # Calcular probabilidades
            probabilidad_local = round(prediccion[0][1] * 100, 2)
            probabilidad_visitante = round(prediccion[0][0] * 100, 2)
        except Exception as e:
            print(f"Error al calcular probabilidades: {e}")

    # Obtener las posiciones de los equipos
    posiciones = Posicion.objects.all().order_by('-puntos')

    # Obtener los videos y convertir URLs de shorts de YouTube
    videos = Video.objects.all()
    for video in videos:
        if "shorts" in video.url:
            video_id = video.url.split('/')[-1]
            video.url = f"https://www.youtube.com/embed/{video_id}"

    return render(
        request,
        'basquetbol/proximo_partido.html',
        {
            'proximo_partido_stats': partido_con_estadisticas,
            'probabilidad_local': probabilidad_local,
            'probabilidad_visitante': probabilidad_visitante,
            'posiciones': posiciones,
            'equipo_inscrito': equipo_inscrito,
            'videos': videos,
        },
    )









def calcular_probabilidades(partido):
    if not partido:
        return 0, 0

    # Cargar el modelo
    model = joblib.load('basquetbol/management/commands/modelo_prediccion_partidos.pkl')

    # Crear un dataframe con las estadísticas necesarias para la predicción
    data = {
        'pases_equipo_local': [partido.estadisticas.pases_equipo_local],
        'faltas_equipo_local': [partido.estadisticas.faltas_equipo_local],
        'triples_equipo_local': [partido.estadisticas.triples_equipo_local],
        'rebotes_equipo_local': [partido.estadisticas.rebotes_equipo_local],
        'puntos_equipo_local': [partido.estadisticas.puntos_equipo_local],
        'pases_equipo_visitante': [partido.estadisticas.pases_equipo_visitante],
        'faltas_equipo_visitante': [partido.estadisticas.faltas_equipo_visitante],
        'triples_equipo_visitante': [partido.estadisticas.triples_equipo_visitante],
        'rebotes_equipo_visitante': [partido.estadisticas.rebotes_equipo_visitante],
        'puntos_equipo_visitante': [partido.estadisticas.puntos_equipo_visitante],
    }

    df = pd.DataFrame(data)

    # Realizar la predicción
    prediccion = model.predict_proba(df)[0]

    # Retornar las probabilidades del equipo local y visitante
    probabilidad_local = round(prediccion[1] * 100, 2)
    probabilidad_visitante = round(prediccion[0] * 100, 2)

    return probabilidad_local, probabilidad_visitante




@login_required
def perfil_usuario(request):
    try:
        entrenador = Entrenador.objects.get(user=request.user)
    except Entrenador.DoesNotExist:
        messages.info(request, "No tienes un equipo inscrito. Por favor, inscribe uno.")
        return redirect('inscribir_equipo')

    equipo = get_object_or_404(Equipo, entrenador=entrenador)

    # Calcular estadísticas generales del equipo
    partidos_jugados = Partido.objects.filter(
        Q(equipo_local=equipo) | Q(equipo_visitante=equipo)
    ).count()




# Vista actualizada
@login_required
def perfil_usuario(request):
    try:
        entrenador = Entrenador.objects.get(user=request.user)
    except Entrenador.DoesNotExist:
        messages.info(request, "No tienes un equipo inscrito. Por favor, inscribe uno.")
        return redirect('inscribir_equipo')

    equipo = get_object_or_404(Equipo, entrenador=entrenador)

    # Formularios
    equipo_form = InscripcionEquipoForm(instance=equipo)
    entrenador_form = EntrenadorForm(instance=entrenador)
    jugador_formset = JugadorFormSet(instance=equipo)

    if request.method == 'POST':
        if 'equipo_form' in request.POST:
            equipo_form = InscripcionEquipoForm(request.POST, request.FILES, instance=equipo)
            if equipo_form.is_valid():
                equipo_form.save()
                messages.success(request, "Información del equipo actualizada correctamente.")
                return redirect('perfil_usuario')

        elif 'entrenador_form' in request.POST:
            entrenador_form = EntrenadorForm(request.POST, instance=entrenador)
            if entrenador_form.is_valid():
                entrenador_form.save()
                messages.success(request, "Información del entrenador actualizada correctamente.")
                return redirect('perfil_usuario')

        elif 'jugador_formset' in request.POST:
            jugador_formset = JugadorFormSet(request.POST, instance=equipo)
            if jugador_formset.is_valid():
                jugador_formset.save()
                messages.success(request, "Jugadores actualizados correctamente.")
                return redirect('perfil_usuario')

    # Obtener estadísticas por fase
    fases = Partido.objects.filter(
        Q(equipo_local=equipo) | Q(equipo_visitante=equipo)
    ).values_list('fase', flat=True).distinct()

    estadisticas_por_fase = {}
    for fase in fases:
        estadisticas_fase = PartidoEstadistica.objects.filter(
            Q(partido__fase=fase) & (Q(partido__equipo_local=equipo) | Q(partido__equipo_visitante=equipo))
        ).aggregate(
            triples_local=Sum('triples_equipo_local', filter=Q(partido__equipo_local=equipo)),
            triples_visitante=Sum('triples_equipo_visitante', filter=Q(partido__equipo_visitante=equipo)),
            puntos_local=Sum('puntos_equipo_local', filter=Q(partido__equipo_local=equipo)),
            puntos_visitante=Sum('puntos_equipo_visitante', filter=Q(partido__equipo_visitante=equipo)),
            faltas_local=Sum('faltas_equipo_local', filter=Q(partido__equipo_local=equipo)),
            faltas_visitante=Sum('faltas_equipo_visitante', filter=Q(partido__equipo_visitante=equipo)),
            rebotes_ofensivos_local=Sum('rebotes_ofensivos_equipo_local', filter=Q(partido__equipo_local=equipo)),
            rebotes_ofensivos_visitante=Sum('rebotes_ofensivos_equipo_visitante', filter=Q(partido__equipo_visitante=equipo)),
            rebotes_defensivos_local=Sum('rebotes_defensivos_equipo_local', filter=Q(partido__equipo_local=equipo)),
            rebotes_defensivos_visitante=Sum('rebotes_defensivos_equipo_visitante', filter=Q(partido__equipo_visitante=equipo)),
            robos_local=Sum('robos_equipo_local', filter=Q(partido__equipo_local=equipo)),
            robos_visitante=Sum('robos_equipo_visitante', filter=Q(partido__equipo_visitante=equipo)),
        )

        estadisticas_por_fase[fase] = {
            'partidos_jugados': Partido.objects.filter(
                Q(fase=fase) & (Q(equipo_local=equipo) | Q(equipo_visitante=equipo))
            ).count(),
            'triples': (estadisticas_fase['triples_local'] or 0) + (estadisticas_fase['triples_visitante'] or 0),
            'puntos': (estadisticas_fase['puntos_local'] or 0) + (estadisticas_fase['puntos_visitante'] or 0),
            'faltas': (estadisticas_fase['faltas_local'] or 0) + (estadisticas_fase['faltas_visitante'] or 0),
            'rebotes_ofensivos': (estadisticas_fase['rebotes_ofensivos_local'] or 0) + (estadisticas_fase['rebotes_ofensivos_visitante'] or 0),
            'rebotes_defensivos': (estadisticas_fase['rebotes_defensivos_local'] or 0) + (estadisticas_fase['rebotes_defensivos_visitante'] or 0),
            'robos': (estadisticas_fase['robos_local'] or 0) + (estadisticas_fase['robos_visitante'] or 0),
        }

    # Próximos partidos
    proximos_partidos = Partido.objects.filter(
        Q(equipo_local=equipo) | Q(equipo_visitante=equipo),
        fecha__gte=timezone.now()
    ).order_by('fecha')

    return render(request, 'basquetbol/perfil_usuario.html', {
        'equipo': equipo,
        'equipo_form': equipo_form,
        'entrenador_form': entrenador_form,
        'jugador_formset': jugador_formset,
        'estadisticas_por_fase': estadisticas_por_fase,
        'proximos_partidos': proximos_partidos,
    })







from django.shortcuts import render, get_object_or_404
from .models import Campeonato, Partido

def seleccionar_campeonato(request):
    campeonato_id = request.GET.get('campeonato_id')  # Obtén el ID del campeonato desde el formulario
    campeonatos = Campeonato.objects.all()
    campeonato = None
    partidos_cuartos, partidos_semifinal, partido_final = [], [], None

    if campeonato_id:
        campeonato = get_object_or_404(Campeonato, id=campeonato_id)
        partidos_cuartos = Partido.objects.filter(campeonato=campeonato, fase='Cuartos').order_by('fecha')
        partidos_semifinal = Partido.objects.filter(campeonato=campeonato, fase='Semifinal').order_by('fecha')
        partido_final = Partido.objects.filter(campeonato=campeonato, fase='Final').first()

    return render(
        request,
        'basquetbol/seleccionar_campeonato.html',
        {
            'campeonatos': campeonatos,
            'campeonato': campeonato,
            'partidos_cuartos': partidos_cuartos,
            'partidos_semifinal': partidos_semifinal,
            'partido_final': partido_final,
            'seleccionado_id': int(campeonato_id) if campeonato_id else None,
        }
    )


from django.shortcuts import render, get_object_or_404
from .models import Campeonato, Partido

from django.http import JsonResponse

from django.shortcuts import render, get_object_or_404
from .models import Campeonato, Partido

from django.shortcuts import render, get_object_or_404
from .models import Campeonato, Partido

def bracket_eliminatorias(request, campeonato_id):
    campeonato = get_object_or_404(Campeonato, id=campeonato_id)

    partidos_cuartos = Partido.objects.filter(campeonato=campeonato, fase='Cuartos').order_by('fecha')
    partidos_semifinal = Partido.objects.filter(campeonato=campeonato, fase='Semifinal').order_by('fecha')
    partido_final = Partido.objects.filter(campeonato=campeonato, fase='Final').first()

    # Obtener todos los campeonatos para el formulario
    todos_los_campeonatos = Campeonato.objects.all()

    context = {
        'campeonato': campeonato,
        'partidos_cuartos': partidos_cuartos,
        'partidos_semifinal': partidos_semifinal,
        'partido_final': partido_final,
        'todos_los_campeonatos': todos_los_campeonatos,
        'seleccionado_id': campeonato.id,  # Pasar el ID seleccionado al contexto
    }

    return render(request, 'basquetbol/bracket.html', context)


def buscar_partidos(request):
    query = request.GET.get('q', '')  # Obtener el término de búsqueda del formulario
    partidos = Partido.objects.all()

    if query:
        partidos = partidos.filter(
            Q(equipo_local__nombre_equipo__icontains=query) |
            Q(equipo_visitante__nombre_equipo__icontains=query)
        )

    return render(request, 'basquetbol/buscar_partidos.html', {
        'partidos': partidos,
        'query': query,
    })






def buscar_partidos(request):
    query = request.GET.get('q', '')  # Obtener el término de búsqueda del formulario
    partidos = Partido.objects.all()

    if query:
        partidos = partidos.filter(
            Q(equipo_local__nombre_equipo__icontains=query) |
            Q(equipo_visitante__nombre_equipo__icontains=query)
        )

    return render(request, 'basquetbol/buscar_partidos.html', {
        'partidos': partidos,
        'query': query,
    })



#---------------------------------------------------------- FIN PAGINA DE INCIO, USUARIO --------------------------------------------------





# -------------------- LOGIN Y REGISTRO -------------------------

from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from basquetbol.models import Campeonato  # Asegúrate de importar el modelo correspondiente

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()

            # Verificar si el usuario está activo
            if not user.is_active:
                messages.error(request, "Tu cuenta no está activa. Por favor, verifica tu correo para activarla.")
                return render(request, 'basquetbol/login.html', {'form': form})

            # Iniciar sesión
            auth_login(request, user)

            # Redirigir al 'next' si está definido
            next_url = request.GET.get('next', None)
            if next_url:
                return redirect(next_url)

            # Obtener el primer campeonato disponible
            campeonato = Campeonato.objects.first()

            # Si no hay campeonatos, redirigir a una página por defecto o mostrar un mensaje
            if not campeonato:
                messages.warning(request, "No hay campeonatos disponibles actualmente.")
                return redirect('inicio')  # Cambia 'inicio' por tu vista de página principal

            # Redirigir según el tipo de usuario
            if user.is_superuser or user.groups.filter(name='Administrador').exists():
                return redirect('gestionar_registros')  # Cambia por la vista adecuada para admin
            elif user.groups.filter(name='Planillero').exists():
                return redirect('lista_partidos', campeonato_id=campeonato.id)
            else:
                return redirect('proximo_partido')  # Para usuarios comunes

        else:
            # Si las credenciales son incorrectas
            messages.error(request, "Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.")
    else:
        form = AuthenticationForm()

    return render(request, 'basquetbol/login.html', {'form': form})


#------------------------------------------------------------------------------
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroForm
from .utils import send_confirmation_email

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']

            # Verificar si el usuario o correo ya existen
            if User.objects.filter(username=username).exists():
                messages.error(request, 'El nombre de usuario ya está en uso.')
                return render(request, 'basquetbol/registro.html', {'form': form})
            elif User.objects.filter(email=email).exists():
                form.add_error('email', 'El correo electrónico ya está en uso.')
                return render(request, 'basquetbol/registro.html', {'form': form})
            else:
                try:
                    # Crear usuario como inactivo
                    user = form.save(commit=False)
                    user.is_active = False
                    user.save()

                    # Enviar correo de confirmación
                    send_confirmation_email(user, request)

                    # Cerrar sesión y dar retroalimentación
                    logout(request)
                    messages.success(request, "Registro exitoso. Por favor, verifica tu correo electrónico para activar tu cuenta.")
                    return render(request, 'basquetbol/registro.html', {'form': RegistroForm()})
                except Exception as e:
                    messages.error(request, f'Hubo un error al procesar el registro: {str(e)}.')
                    return render(request, 'basquetbol/registro.html', {'form': form})
    else:
        form = RegistroForm()

    # Renderizar la página de registro con el formulario inicial
    return render(request, 'basquetbol/registro.html', {'form': form})

#---------------------------CONFIRMACIÓN DE EMAIL------------------------------
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect

def confirmar_correo(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)

        if default_token_generator.check_token(user, token):
            user.is_active = True  # Activar la cuenta
            user.save()
            messages.success(request, '¡Cuenta activada exitosamente! Ahora puedes iniciar sesión.')
            return redirect('login')
        else:
            messages.error(request, 'El enlace de activación es inválido o ha expirado.')
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        messages.error(request, 'Hubo un error al intentar activar tu cuenta. Por favor, contacta al soporte.')

    return redirect('login')




# ------------------------------------------------- FIN LOGIN Y REGISTRO -------------------------------------------------------------------



# ------------------------------------------------- Campeonatos -------------------------------------------------------------------



# Vista para inscribir un equipo en un campeonato
@login_required
def inscribir_equipo(request):
    if request.method == 'POST':
        equipo_form = InscripcionEquipoForm(request.POST, request.FILES)
        entrenador_form = EntrenadorForm(request.POST)
        jugador_formset = JugadorFormSet(request.POST)

        if equipo_form.is_valid() and entrenador_form.is_valid() and jugador_formset.is_valid():
            # Crear un nuevo entrenador asociado al usuario
            entrenador = entrenador_form.save(commit=False)
            entrenador.user = request.user  # Asociar el entrenador al usuario actual
            entrenador.save()

            # Crear un nuevo equipo asociado al entrenador
            equipo = equipo_form.save(commit=False)
            equipo.entrenador = entrenador  # Asociar el equipo al entrenador
            equipo.save()

            # Guardar los jugadores asociados al equipo
            jugadores = jugador_formset.save(commit=False)
            for jugador in jugadores:
                jugador.equipo = equipo
                jugador.save()

            messages.success(request, "Equipo inscrito exitosamente.")
            return redirect('proximo_partido')
        else:
            messages.error(request, "Hubo un problema con el formulario. Por favor verifica los campos.")
    else:
        # Inicializar los formularios para una nueva inscripción
        equipo_form = InscripcionEquipoForm()
        entrenador_form = EntrenadorForm()
        jugador_formset = JugadorFormSet()

    return render(request, 'basquetbol/inscribir_equipo.html', {
        'equipo_form': equipo_form,
        'entrenador_form': entrenador_form,
        'jugador_formset': jugador_formset
    })





# Vista para crear un nuevo campeonato
def crear_campeonato(request):
    if request.method == 'POST':
        form = CrearCampeonatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_campeonatos')
        else:
            # Mostrar errores en la consola para depuración
            print("Errores en el formulario: ", form.errors)
    else:
        form = CrearCampeonatoForm()

    return render(request, 'basquetbol/crear_campeonato.html', {'form': form})




# Vista para listar todos los campeonatos
def lista_campeonatos(request):
    campeonatos = Campeonato.objects.all()
    return render(request, 'basquetbol/lista_campeonatos.html', {'campeonatos': campeonatos})





def detalle_campeonato(request, campeonato_id):
    campeonato = get_object_or_404(Campeonato, id=campeonato_id)
    equipos = Equipo.objects.filter(campeonato=campeonato)

    # Verificar si ya existen partidos para la fase clasificatoria de este campeonato
    partidos_clasificatorias = Partido.objects.filter(campeonato=campeonato, fase='Clasificatorias')

    # Obtener el campeón si existe
    campeon = None
    try:
        campeon = Campeon.objects.get(campeonato=campeonato)
    except Campeon.DoesNotExist:
        campeon = None

    return render(request, 'basquetbol/detalle_campeonato.html', {
        'campeonato': campeonato,
        'equipos': equipos,
        'partidos_clasificatorias': partidos_clasificatorias,
        'partidos_clasificatorias_creados': partidos_clasificatorias.exists(),
        'campeon': campeon,
    })
    
    
    
@login_required
def abandonar_campeonato(request):
    # Obtener el equipo asociado al entrenador del usuario
    equipo = get_object_or_404(Equipo, entrenador__user=request.user)

    if request.method == 'POST':
        # Eliminar los jugadores asociados al equipo
        jugadores = Jugador.objects.filter(equipo=equipo)
        for jugador in jugadores:
            jugador.delete()

        # Eliminar el entrenador asociado al equipo
        entrenador = equipo.entrenador
        equipo.delete()  # Primero eliminamos el equipo

        # Después eliminamos el entrenador si existe
        if entrenador:
            entrenador.delete()

        messages.success(request, "Has abandonado el campeonato, y tu equipo y entrenador han sido eliminados.")
        return redirect('proximo_partido')

    return render(request, 'basquetbol/abandonar_campeonato.html', {'equipo': equipo})
    



@login_required
def generar_partidos_clasificatorias_view(request, campeonato_id):
    campeonato = get_object_or_404(Campeonato, id=campeonato_id)

    # Verificar si el usuario tiene permisos suficientes
    if not request.user.is_superuser:
        messages.error(request, "No tienes permiso para generar partidos.")
        return redirect('gestionar_registros')

    # Verificar si ya existen partidos de la fase clasificatoria para este campeonato
    if Partido.objects.filter(campeonato=campeonato, fase='Clasificatorias').exists():
        messages.warning(request, "Los partidos de la fase clasificatoria ya han sido creados.")
        return redirect('gestionar_registros')

    # Obtener los equipos del campeonato
    equipos = list(Equipo.objects.filter(campeonato=campeonato))
    if len(equipos) < 2:
        messages.warning(request, "No hay suficientes equipos para generar partidos.")
        return redirect('gestionar_registros')

    # Generar combinaciones de partidos y limitar a 3 partidos por equipo
    partidos = []
    equipo_partidos = {equipo: 0 for equipo in equipos}  # Llevar un registro de cuántos partidos ha jugado cada equipo
    posibles_partidos = list(combinations(equipos, 2))
    shuffle(posibles_partidos)  # Mezclar para obtener combinaciones aleatorias

    # Crear partidos asegurando que cada equipo solo juegue tres veces
    for equipo_local, equipo_visitante in posibles_partidos:
        if equipo_partidos[equipo_local] < 3 and equipo_partidos[equipo_visitante] < 3:
            partidos.append((equipo_local, equipo_visitante))
            equipo_partidos[equipo_local] += 1
            equipo_partidos[equipo_visitante] += 1
        # Romper el bucle si todos los equipos han alcanzado el límite de 3 partidos
        if all(partidos_count == 3 for partidos_count in equipo_partidos.values()):
            break

    # Asignar fechas y estadios a los partidos
    fecha_base = campeonato.fecha_inicio
    for i, (equipo_local, equipo_visitante) in enumerate(partidos):
        fecha_partido = fecha_base + timedelta(days=i)
        estadio = choice(Estadio.objects.all()) if Estadio.objects.exists() else None

        Partido.objects.create(
            equipo_local=equipo_local,
            equipo_visitante=equipo_visitante,
            fecha=fecha_partido,
            fase='Clasificatorias',
            campeonato=campeonato,
            estadio=estadio
        )

    messages.success(request, "Partidos de la fase clasificatoria generados exitosamente.")
    # No redirigir a otra página, sino volver a renderizar la página de gestionar registros
    return redirect('gestionar_registros')




@login_required
@user_passes_test(lambda u: u.groups.filter(name='Administrador').exists())
def generar_fase_eliminatoria(request, campeonato_id):
    campeonato = get_object_or_404(Campeonato, id=campeonato_id)

    # Obtener los 8 equipos mejor clasificados
    posiciones = campeonato.posicion_set.order_by('-puntos')[:8]
    equipos = [posicion.equipo for posicion in posiciones]

    if len(equipos) < 8:
        messages.error(request, "No hay suficientes equipos para generar la fase eliminatoria.")
        return redirect('detalle_campeonato', campeonato_id=campeonato.id)

    # Definir una fecha base a partir de la cual asignar fechas para los partidos
    fecha_base = timezone.now()

    # Generar los partidos para los cuartos de final (antes llamado octavos)
    for i in range(4):
        equipo_local = equipos[i]
        equipo_visitante = equipos[7 - i]  # Emparejar 1-8, 2-7, 3-6, 4-5

        # Asignar una fecha para el partido, incrementando la fecha base por días
        fecha_partido = fecha_base + timedelta(days=i)

        # Crear el partido y la estadística asociada
        partido = Partido.objects.create(
            campeonato=campeonato,
            equipo_local=equipo_local,
            equipo_visitante=equipo_visitante,
            fase='Cuartos',  # Cambiado de 'Octavos' a 'Cuartos'
            fecha=fecha_partido  # Asignar la fecha al partido
        )
        PartidoEstadistica.objects.create(partido=partido)  # Crear la estadística para el partido

    messages.success(request, f"Partidos de cuartos de final generados exitosamente.")
    return redirect('detalle_campeonato', campeonato_id=campeonato.id)




@login_required
@user_passes_test(lambda u: u.groups.filter(name='Administrador').exists())
def avanzar_fase_eliminatoria(request, campeonato_id, fase_actual):
    campeonato = get_object_or_404(Campeonato, id=campeonato_id)

    # Obtener los partidos de la fase actual
    partidos = Partido.objects.filter(campeonato=campeonato, fase=fase_actual)

    if not partidos.exists():
        messages.error(request, "No hay partidos disponibles para esta fase.")
        return redirect('detalle_campeonato', campeonato_id=campeonato.id)

    ganadores = []
    for partido in partidos:
        estadisticas = partido.estadisticas  # Acceder a las estadísticas del partido
        if estadisticas.puntos_equipo_local > estadisticas.puntos_equipo_visitante:
            ganadores.append(partido.equipo_local)
        elif estadisticas.puntos_equipo_visitante > estadisticas.puntos_equipo_local:
            ganadores.append(partido.equipo_visitante)
        else:
            messages.error(request, f"El partido entre {partido.equipo_local} y {partido.equipo_visitante} está empatado. No se puede avanzar a la siguiente fase sin un ganador.")
            return redirect('detalle_campeonato', campeonato_id=campeonato.id)

    # Verificar a qué fase se debe avanzar
    nueva_fase = ''
    if fase_actual == 'Cuartos':
        nueva_fase = 'Semifinal'
    elif fase_actual == 'Semifinal':
        nueva_fase = 'Final'
    elif fase_actual == 'Final':
        messages.success(request, "El campeonato ha concluido.")
        return redirect('detalle_campeonato', campeonato_id=campeonato.id)

    # Definir una fecha base a partir de la cual asignar fechas para los partidos
    fecha_base = timezone.now()

    # Generar los partidos para la nueva fase
    for i in range(0, len(ganadores), 2):
        fecha_partido = fecha_base + timedelta(days=i)

        partido = Partido.objects.create(
            campeonato=campeonato,
            equipo_local=ganadores[i],
            equipo_visitante=ganadores[i + 1],
            fase=nueva_fase,
            fecha=fecha_partido  # Asignar la fecha al partido
        )
        PartidoEstadistica.objects.create(partido=partido)  # Crear la estadística para el nuevo partido

    messages.success(request, f"Partidos de {nueva_fase} generados exitosamente.")
    return redirect('detalle_campeonato', campeonato_id=campeonato.id)





def octavos_view(request, campeonato_id):
    campeonato = get_object_or_404(Campeonato, id=campeonato_id)
    partidos_octavos = Partido.objects.filter(campeonato=campeonato, fase='Octavos')

    context = {
        'campeonato': campeonato,
        'partidos_octavos': partidos_octavos,
    }

    return render(request, 'basquetbol/octavos.html', context)





def actualizar_posiciones(partido):
    # Obtener las estadísticas del partido
    estadisticas = PartidoEstadistica.objects.filter(partido=partido).first()

    if not estadisticas:
        # Si no hay estadísticas registradas para el partido, no se puede actualizar la posición
        return

    # Obtener los equipos
    equipo_local = partido.equipo_local
    equipo_visitante = partido.equipo_visitante

    # Verificar el resultado del partido basado en los puntos anotados
    puntos_local = estadisticas.puntos_equipo_local
    puntos_visitante = estadisticas.puntos_equipo_visitante

    if puntos_local > puntos_visitante:
        # Equipo local gana
        actualizar_puntuacion(partido.campeonato, equipo_local, 3, True)
        actualizar_puntuacion(partido.campeonato, equipo_visitante, 0, False)
    elif puntos_visitante > puntos_local:
        # Equipo visitante gana
        actualizar_puntuacion(partido.campeonato, equipo_visitante, 3, True)
        actualizar_puntuacion(partido.campeonato, equipo_local, 0, False)
    else:
        # Si es empate
        actualizar_puntuacion(partido.campeonato, equipo_local, 1, False)
        actualizar_puntuacion(partido.campeonato, equipo_visitante, 1, False)


def actualizar_puntuacion(campeonato, equipo, puntos, ganador):
    # Actualizar o crear la posición del equipo en el campeonato específico
    posicion, creada = Posicion.objects.get_or_create(equipo=equipo, campeonato=campeonato)
    
    # Actualizar los valores
    posicion.puntos += puntos
    posicion.partidos_jugados += 1
    if ganador:
        posicion.partidos_ganados += 1
    else:
        posicion.partidos_perdidos += 1
    
    # Guardar los cambios
    posicion.save()






def tabla_posiciones_view(request, campeonato_id):
    campeonato = get_object_or_404(Campeonato, id=campeonato_id)
    posiciones = Posicion.objects.filter(campeonato=campeonato).order_by('-puntos', '-partidos_ganados')

    return render(request, 'basquetbol/tabla_posiciones.html', {
        'campeonato': campeonato,
        'posiciones': posiciones,
    })






@login_required
@user_passes_test(lambda u: u.groups.filter(name='Planillero').exists())  # Solo usuarios 'Planillero'
def lista_partidos(request, campeonato_id=None):
    if campeonato_id:
        campeonato = get_object_or_404(Campeonato, id=campeonato_id)
        partidos = Partido.objects.filter(campeonato=campeonato).order_by('fecha')
    else:
        partidos = Partido.objects.all().order_by('fecha')
        campeonato = None
    
    context = {
        'campeonato': campeonato,
        'partidos': partidos,
    }
    return render(request, 'basquetbol/lista_partidos.html', context)






def campeonatos_view(request, campeonato_id):
    campeonato = get_object_or_404(Campeonato, id=campeonato_id)
    
    # Actualizar la fase de los partidos
    actualizar_fase_partidos(campeonato)

    # Obtener partidos de cada fase
    partidos_clasificatorias = Partido.objects.filter(campeonato=campeonato, fase='Clasificatorias')
    partidos_cuartos = Partido.objects.filter(campeonato=campeonato, fase='Cuartos')
    partidos_semifinal = Partido.objects.filter(campeonato=campeonato, fase='Semifinal')
    partidos_final = Partido.objects.filter(campeonato=campeonato, fase='Final')

    context = {
        'campeonato': campeonato,
        'partidos_clasificatorias': partidos_clasificatorias,
        'partidos_cuartos': partidos_cuartos,
        'partidos_semifinal': partidos_semifinal,
        'partidos_final': partidos_final,
    }

    return render(request, 'basquetbol/campeonato_bracket.html', context)






def actualizar_fase_partidos(campeonato):
    # Obtener partidos de la fase de Cuartos y determinar los ganadores si no están definidos
    partidos_cuartos = Partido.objects.filter(campeonato=campeonato, fase='Cuartos')
    ganadores_cuartos = []

    for partido in partidos_cuartos:
        if partido.goles_local is not None and partido.goles_visitante is not None:
            if partido.goles_local > partido.goles_visitante:
                ganadores_cuartos.append(partido.equipo_local)
            elif partido.goles_visitante > partido.goles_local:
                ganadores_cuartos.append(partido.equipo_visitante)

    # Si los partidos de Semifinal aún no existen y tenemos 4 ganadores
    if not Partido.objects.filter(campeonato=campeonato, fase='Semifinal').exists() and len(ganadores_cuartos) == 4:
        for i in range(0, len(ganadores_cuartos), 2):
            Partido.objects.create(
                campeonato=campeonato,
                equipo_local=ganadores_cuartos[i],
                equipo_visitante=ganadores_cuartos[i + 1],
                fecha=None,
                estadio=None,
                fase='Semifinal'
            )


# ------------------------------------------------------- FIN CAMPEONATO --------------------------------------------------------------------------------------



#------------------------------------------------------- ADMINISTRADOR Y PLANILLERO -------------------------------------------------------------------------------
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import Partido, PartidoEstadistica
from .forms import PartidoStatsForm
from django.db import transaction


@login_required
@user_passes_test(lambda u: u.groups.filter(name='Planillero').exists())  # Solo usuarios 'Planillero'
def registrar_estadisticas_partido(request, partido_id):
    # Obtener el partido
    partido = get_object_or_404(Partido, id=partido_id)

    # Crear o recuperar las estadísticas del partido
    estadisticas, created = PartidoEstadistica.objects.get_or_create(partido=partido)

    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        equipo = request.POST.get('equipo')  # 'local' o 'visitante'
        accion = request.POST.get('accion')  # 'add' o 'subtract'

        try:
            # Actualizar los puntos según el equipo y acción
            if equipo == 'local':
                if accion == 'add':
                    estadisticas.puntos_equipo_local += 1
                elif accion == 'subtract' and estadisticas.puntos_equipo_local > 0:
                    estadisticas.puntos_equipo_local -= 1
            elif equipo == 'visitante':
                if accion == 'add':
                    estadisticas.puntos_equipo_visitante += 1
                elif accion == 'subtract' and estadisticas.puntos_equipo_visitante > 0:
                    estadisticas.puntos_equipo_visitante -= 1
            else:
                return JsonResponse({'error': 'Equipo inválido'}, status=400)

            # Guardar las estadísticas actualizadas
            estadisticas.save()

            # Actualizar las posiciones si el partido pertenece a las clasificatorias
            if partido.fase == 'Clasificatorias':
                actualizar_posiciones(partido)

            return JsonResponse({
                'puntos_local': estadisticas.puntos_equipo_local,
                'puntos_visitante': estadisticas.puntos_equipo_visitante,
            })

        except Exception as e:
            return JsonResponse({'error': f'Error al actualizar puntos: {str(e)}'}, status=400)

    # Procesar solicitudes normales (no AJAX)
    if request.method == 'POST':
        form = PartidoStatsForm(request.POST, instance=estadisticas)
        if form.is_valid():
            with transaction.atomic():  # Usar transacción para garantizar consistencia
                form.save()
                # Actualizar posiciones solo si es clasificatoria
                if partido.fase == 'Clasificatorias':
                    actualizar_posiciones(partido)
            messages.success(request, "Estadísticas registradas y posiciones actualizadas correctamente.")
            return redirect('lista_partidos', campeonato_id=partido.campeonato.id)
        else:
            return render(request, 'basquetbol/registrar_estadisticas.html', {
                'form': form,
                'partido': partido,
                'errors': form.errors,
            })

    # Renderizar el formulario con los datos actuales
    form = PartidoStatsForm(instance=estadisticas)
    return render(request, 'basquetbol/registrar_estadisticas.html', {
        'form': form,
        'partido': partido,
    })




from .models import Video  # Importa el modelo de Video

@login_required
@user_passes_test(lambda u: u.is_superuser or u.groups.filter(name='Administrador').exists())
def gestionar_registros(request):
    usuario_form = RegistroForm()
    equipo_form = InscripcionEquipoForm()
    entrenador_form = EntrenadorForm()
    jugador_formset = JugadorFormSet()
    campeonato_form = CrearCampeonatoForm()

    campeonatos = Campeonato.objects.all()
    equipos = Equipo.objects.all()
    posiciones = Posicion.objects.all().order_by('-puntos', '-partidos_ganados')
    videos = Video.objects.all()

    campeonato_seleccionado = None
    partidos_clasificatorias = []
    partidos_eliminatoria = []

    if request.method == 'POST':
        # Manejo del detalle del campeonato
        if 'campeonato_id' in request.POST:
            campeonato_id = request.POST.get('campeonato_id')
            if campeonato_id:
                try:
                    campeonato_seleccionado = Campeonato.objects.get(id=campeonato_id)
                    partidos_clasificatorias = Partido.objects.filter(campeonato=campeonato_seleccionado, fase='Clasificatorias')
                    partidos_eliminatoria = Partido.objects.filter(campeonato=campeonato_seleccionado, fase='Eliminatoria')
                except Campeonato.DoesNotExist:
                    messages.error(request, "El campeonato seleccionado no existe.")

    context = {
        'usuario_form': usuario_form,
        'equipo_form': equipo_form,
        'entrenador_form': entrenador_form,
        'jugador_formset': jugador_formset,
        'campeonato_form': campeonato_form,
        'campeonatos': campeonatos,
        'equipos': equipos,
        'posiciones': posiciones,
        'videos': videos,
    }

    if campeonato_seleccionado:
        context.update({
            'campeonato_seleccionado': campeonato_seleccionado,
            'partidos_clasificatorias': partidos_clasificatorias,
            'partidos_eliminatoria': partidos_eliminatoria,
        })

    return render(request, 'basquetbol/gestionar_registros.html', context)



@login_required
def modificar_equipo(request):
    equipos = Equipo.objects.all()  # Lista de todos los equipos
    equipo_seleccionado = None
    equipo_form = None
    entrenador_form = None

    if request.method == 'POST' and 'equipo_select' in request.POST:
        equipo_id = request.POST.get('equipo_select')
        if equipo_id:
            equipo_seleccionado = get_object_or_404(Equipo, id=equipo_id)
            equipo_form = InscripcionEquipoForm(instance=equipo_seleccionado)
            entrenador_form = EntrenadorForm(instance=equipo_seleccionado.entrenador)

    elif request.method == 'POST' and 'modificar_equipo' in request.POST:
        equipo_id = request.POST.get('equipo_select')
        equipo_seleccionado = get_object_or_404(Equipo, id=equipo_id)
        equipo_form = InscripcionEquipoForm(request.POST, instance=equipo_seleccionado)
        entrenador_form = EntrenadorForm(request.POST, instance=equipo_seleccionado.entrenador)

        if equipo_form.is_valid() and entrenador_form.is_valid():
            equipo_form.save()
            entrenador_form.save()
            messages.success(request, 'Equipo modificado correctamente')
            return redirect('modificar_equipo')

    context = {
        'equipos': equipos,
        'equipo_seleccionado': equipo_seleccionado,
        'equipo_form': equipo_form,
        'entrenador_form': entrenador_form,
    }

    return render(request, 'basquetbol/modificar_equipo.html', context)






@login_required
def modificar_equipo(request):
    if request.method == 'POST' and 'modificar_equipo' in request.POST:
        equipo_id = request.POST.get('equipo_select')
        equipo = get_object_or_404(Equipo, id=equipo_id)

        # Actualizar datos del equipo
        equipo.nombre_equipo = request.POST.get('nombre_equipo', equipo.nombre_equipo)
        
        # Actualizar o crear un entrenador
        entrenador_nombre = request.POST.get('entrenador_nombre', '')
        if entrenador_nombre:
            if equipo.entrenador:
                equipo.entrenador.nombre_entrenador = entrenador_nombre
                equipo.entrenador.save()
            else:
                entrenador = Entrenador(nombre_entrenador=entrenador_nombre)
                entrenador.save()
                equipo.entrenador = entrenador
        
        equipo.save()
        messages.success(request, 'Equipo actualizado exitosamente.')
        return redirect('gestionar_registros')

    equipos = Equipo.objects.all()
    return render(request, 'basquetbol/gestionar_registros.html', {
        'equipos': equipos,
        # Otras variables del contexto
    })





@login_required
@user_passes_test(lambda u: u.groups.filter(name='Planillero').exists())  # Verificar que el usuario pertenece al grupo 'Planillero'
def seleccionar_partido(request):
    # Obtener todos los partidos que aún no tienen estadísticas registradas
    partidos = Partido.objects.filter(estadistica__isnull=True).order_by('fecha')

    context = {
        'partidos': partidos
    }

    return render(request, 'basquetbol/seleccionar_partido.html', context)


#------------------------------------------------------- FIN ADMINISTRADOR Y PLANILLERO -------------------------------------------------------------------------------


from django.db.models import Sum, F

def estadisticas_equipos(request):
    equipos = Equipo.objects.annotate(
        total_puntos_local=Sum('partidos_local__estadisticas__puntos_equipo_local'),
        total_puntos_visitante=Sum('partidos_visitante__estadisticas__puntos_equipo_visitante'),
        total_triples_local=Sum('partidos_local__estadisticas__triples_equipo_local'),
        total_triples_visitante=Sum('partidos_visitante__estadisticas__triples_equipo_visitante'),
        total_pases_local=Sum('partidos_local__estadisticas__pases_equipo_local'),
        total_pases_visitante=Sum('partidos_visitante__estadisticas__pases_equipo_visitante'),
        total_rebotes_local=Sum(
            'partidos_local__estadisticas__rebotes_ofensivos_equipo_local') +
            Sum('partidos_local__estadisticas__rebotes_defensivos_equipo_local'),
        total_rebotes_visitante=Sum(
            'partidos_visitante__estadisticas__rebotes_ofensivos_equipo_visitante') +
            Sum('partidos_visitante__estadisticas__rebotes_defensivos_equipo_visitante'),
        total_faltas_local=Sum('partidos_local__estadisticas__faltas_equipo_local'),
        total_faltas_visitante=Sum('partidos_visitante__estadisticas__faltas_equipo_visitante'),
        total_robos_local=Sum('partidos_local__estadisticas__robos_equipo_local'),
        total_robos_visitante=Sum('partidos_visitante__estadisticas__robos_equipo_visitante'),
    ).annotate(
        total_puntos=F('total_puntos_local') + F('total_puntos_visitante'),
        total_triples=F('total_triples_local') + F('total_triples_visitante'),
        total_pases=F('total_pases_local') + F('total_pases_visitante'),
        total_rebotes=F('total_rebotes_local') + F('total_rebotes_visitante'),
        total_faltas=F('total_faltas_local') + F('total_faltas_visitante'),
        total_robos=F('total_robos_local') + F('total_robos_visitante'),
    ).order_by('-total_puntos')

    return render(request, 'basquetbol/estadisticas_equipos.html', {
        'equipos': equipos,
    })


from django.http import JsonResponse
from .models import Equipo, Partido

from django.db.models import F, Sum, Avg, Q
from django.http import JsonResponse
from .models import Equipo, Partido

from django.http import JsonResponse
from django.db.models import F, Sum

from django.http import JsonResponse
from django.db.models import F

def estadisticas_equipo_api(request, equipo_id):
    try:
        equipo = Equipo.objects.get(id=equipo_id)

        # Obtener partidos como local y visitante
        partidos_local = equipo.partidos_local.select_related('estadisticas').all()
        partidos_visitante = equipo.partidos_visitante.select_related('estadisticas').all()
        partidos = list(partidos_local) + list(partidos_visitante)

        # Calcular partidos ganados
        ganados_local = partidos_local.filter(
            estadisticas__puntos_equipo_local__gt=F('estadisticas__puntos_equipo_visitante')
        ).count()
        ganados_visitante = partidos_visitante.filter(
            estadisticas__puntos_equipo_visitante__gt=F('estadisticas__puntos_equipo_local')
        ).count()
        partidos_ganados = ganados_local + ganados_visitante

        # Totales y promedios
        totales = {
            'puntos': sum(
                p.estadisticas.puntos_equipo_local if p.equipo_local == equipo else p.estadisticas.puntos_equipo_visitante
                for p in partidos
            ),
            'triples': sum(
                p.estadisticas.triples_equipo_local if p.equipo_local == equipo else p.estadisticas.triples_equipo_visitante
                for p in partidos
            ),
            'pases': sum(
                p.estadisticas.pases_equipo_local if p.equipo_local == equipo else p.estadisticas.pases_equipo_visitante
                for p in partidos
            ),
            'rebotes_ofensivos': sum(
                p.estadisticas.rebotes_ofensivos_equipo_local if p.equipo_local == equipo else p.estadisticas.rebotes_ofensivos_equipo_visitante
                for p in partidos
            ),
            'rebotes_defensivos': sum(
                p.estadisticas.rebotes_defensivos_equipo_local if p.equipo_local == equipo else p.estadisticas.rebotes_defensivos_equipo_visitante
                for p in partidos
            ),
        }
        totales['rebotes'] = totales['rebotes_ofensivos'] + totales['rebotes_defensivos']

        total_partidos = len(partidos)
        promedios = {key: (value / total_partidos if total_partidos > 0 else 0) for key, value in totales.items()}

        # Datos para los gráficos
        data = {
            'estadisticas_totales': {**totales, 'ganados': partidos_ganados},
            'estadisticas_promedios': promedios,
            'rebotes': {
                'ofensivos': totales['rebotes_ofensivos'],
                'defensivos': totales['rebotes_defensivos']
            },
            'partidos': [
                {
                    'partido': f"{p.equipo_local.nombre_equipo} vs {p.equipo_visitante.nombre_equipo}",
                    'ganado': int(
                        (p.equipo_local == equipo and p.estadisticas.puntos_equipo_local > p.estadisticas.puntos_equipo_visitante) or
                        (p.equipo_visitante == equipo and p.estadisticas.puntos_equipo_visitante > p.estadisticas.puntos_equipo_local)
                    ),
                    'puntos': p.estadisticas.puntos_equipo_local if p.equipo_local == equipo else p.estadisticas.puntos_equipo_visitante,
                    'triples': p.estadisticas.triples_equipo_local if p.equipo_local == equipo else p.estadisticas.triples_equipo_visitante,
                }
                for p in partidos
            ],
        }

        return JsonResponse(data)

    except Equipo.DoesNotExist:
        return JsonResponse({'error': 'Equipo no encontrado'}, status=404)
    except Exception as e:
        return JsonResponse({'error': f'Error al procesar la solicitud: {str(e)}'}, status=500)




@login_required
def foro(request):
    if request.method == "POST":
        # Procesar formulario de nueva publicación
        publicacion_form = PublicacionForm(request.POST)
        if publicacion_form.is_valid():
            nueva_publicacion = publicacion_form.save(commit=False)
            nueva_publicacion.autor = request.user  # Asignar el autor como el usuario actual
            nueva_publicacion.save()
            return redirect('foro')
    else:
        publicacion_form = PublicacionForm()

    # Obtener todas las publicaciones ordenadas por fecha de creación
    publicaciones = Publicacion.objects.all().order_by('-fecha_creacion')

    # Formulario para agregar comentarios
    comentario_form = ComentarioForm()

    return render(request, 'basquetbol/foro.html', {
        'publicaciones': publicaciones,
        'publicacion_form': publicacion_form,
        'comentario_form': comentario_form,
    })

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Publicacion
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Publicacion

@login_required
def like_publicacion(request):
    if request.method == "POST":
        # Recuperar el ID de la publicación desde el formulario
        publicacion_id = request.POST.get("publicacion_id")
        
        if not publicacion_id:
            return JsonResponse({"success": False, "error": "No se proporcionó el ID de la publicación"})
        
        # Obtener la publicación correspondiente
        try:
            publicacion = Publicacion.objects.get(id=publicacion_id)
        except Publicacion.DoesNotExist:
            return JsonResponse({"success": False, "error": "La publicación no existe"})
        
        # Verificar si el usuario ya ha dado like y actualizarlo
        if request.user in publicacion.likes.all():
            publicacion.likes.remove(request.user)
            liked = False
        else:
            publicacion.likes.add(request.user)
            liked = True
        
        # Responder con la información actualizada
        return JsonResponse({"success": True, "liked": liked, "total_likes": publicacion.likes.count()})
    
    return JsonResponse({"success": False, "error": "Solicitud inválida"})

from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from .models import Publicacion, Comentario
from .forms import ComentarioForm
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Publicacion, Comentario
from .forms import ComentarioForm

def agregar_comentario(request):
    if request.method == 'POST':
        publicacion_id = request.POST.get('publicacion_id')
        contenido = request.POST.get('contenido')
        publicacion = get_object_or_404(Publicacion, id=publicacion_id)

        if contenido.strip():  # Asegurarte de que no sea solo espacios en blanco
            comentario = Comentario.objects.create(
                contenido=contenido,
                autor=request.user,
                publicacion=publicacion
            )
            return JsonResponse({
                'success': True,
                'autor': comentario.autor.username,
                'contenido': comentario.contenido,
                'fecha_creacion': comentario.fecha_creacion.strftime("%d %b %Y, %H:%M")
            })

        return JsonResponse({'success': False, 'error': 'El contenido del comentario no puede estar vacío.'})

    return JsonResponse({'success': False, 'error': 'Método no permitido.'})

from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from .models import Publicacion, Comentario
def eliminar_publicacion(request, publicacion_id):
    if request.method == "POST":
        publicacion = get_object_or_404(Publicacion, id=publicacion_id)
        if request.user == publicacion.autor:
            publicacion.delete()
            return JsonResponse({'success': True, 'message': 'Publicación eliminada exitosamente.'})
        else:
            return JsonResponse({'success': False, 'message': 'No tienes permiso para eliminar esta publicación.'})
    return JsonResponse({'success': False, 'message': 'Método no permitido.'})

def eliminar_comentario(request, comentario_id):
    if request.method == "POST":
        comentario = get_object_or_404(Comentario, id=comentario_id)
        if request.user == comentario.autor:
            comentario.delete()
            return JsonResponse({'success': True, 'message': 'Comentario eliminado exitosamente.'})
        else:
            return JsonResponse({'success': False, 'message': 'No tienes permiso para eliminar este comentario.'})
    return JsonResponse({'success': False, 'message': 'Método no permitido.'})