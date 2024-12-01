
#-------------------------- IMPORTS --------------------------
from django.utils.encoding import force_bytes

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
from .models import (
    Equipo, Jugador, Entrenador, Campeonato, Partido, Posicion, Campeon, PartidoEstadistica, Estadio, Post, Reply
)
from .forms import (
    InscripcionEquipoForm, EntrenadorForm, JugadorFormSet, CrearCampeonatoForm, RegistroForm, PartidoStatsForm
)

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .models import Equipo, Video  # Importa el modelo Video

#---------------------------------------------- FIN IMPORTS --------------------------------------------------





#------------------------- keiji ------------------------------------------------------------------------

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Reply

def foro(request):
    posts = Post.objects.all().order_by('-created_at')  # Obtén las publicaciones
    print(posts)  # Depura las publicaciones en la consola
    return render(request, 'basquetbol/foro.html', {'posts': posts})  # Pásalas al contexto


@login_required
def create_post(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Post.objects.create(author=request.user, content=content)
        return redirect('foro')

@login_required
def like_post(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        if request.user in post.likes.all():
            post.likes.remove(request.user)
            liked = False
        else:
            post.likes.add(request.user)
            liked = True

        # Retorna el conteo de likes y el estado de "like"
        return JsonResponse({'liked': liked, 'like_count': post.likes.count()})

@login_required
def reply_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Reply.objects.create(post=post, author=request.user, content=content)
    return redirect('foro')

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Verifica que el usuario autenticado sea el autor del post
    if post.author == request.user:
        post.delete()
        return redirect('foro')  # Redirige a la lista de posts después de eliminar
    else:
        return render(request, 'error.html', {'message': 'No tienes permiso para eliminar este post.'})




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


from django.utils.timezone import now
import pandas as pd
import joblib
from .models import Partido, Video, Posicion, Equipo

def proximo_partido(request):
    # Verificar si el usuario tiene un equipo inscrito
    equipo_inscrito = (
        Equipo.objects.filter(entrenador__user=request.user).exists()
        if request.user.is_authenticated
        else False
    )

    # Obtener todos los partidos con estadísticas registradas
    partidos_con_estadisticas = Partido.objects.filter(estadisticas__isnull=False).order_by('fecha')

    # Obtener el partido más cercano a la fecha actual sin estadísticas registradas
    partido_proximo = (
        Partido.objects.filter(fecha__gte=now(), estadisticas__isnull=True)
        .order_by('fecha')
        .first()
    )

    # Inicializar probabilidades como vacías
    probabilidad_local = "No dsponible "
    probabilidad_visitante = "No dsponible "

    # Solo calcular probabilidades si el partido tiene estadísticas
    if partido_proximo and hasattr(partido_proximo, 'estadisticas'):
        model = joblib.load('modelo_prediccion_partidos.pkl')
        estadisticas = partido_proximo.estadisticas
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

        probabilidad_local = round(prediccion[0][1] * 100, 2)
        probabilidad_visitante = round(prediccion[0][0] * 100, 2)

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
            'partidos_con_estadisticas': partidos_con_estadisticas,
            'proximo_partido': partido_proximo,
            'probabilidad_local': probabilidad_local,
            'probabilidad_visitante': probabilidad_visitante,
            'posiciones': posiciones,
            'equipo_inscrito': equipo_inscrito,
            'videos': videos,
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
            rebotes_local=Sum('rebotes_equipo_local', filter=Q(partido__equipo_local=equipo)),
            rebotes_visitante=Sum('rebotes_equipo_visitante', filter=Q(partido__equipo_visitante=equipo)),
        )

        estadisticas_por_fase[fase] = {
            'partidos_jugados': Partido.objects.filter(
                Q(fase=fase) & (Q(equipo_local=equipo) | Q(equipo_visitante=equipo))
            ).count(),
            'triples': (estadisticas_fase['triples_local'] or 0) + (estadisticas_fase['triples_visitante'] or 0),
            'puntos': (estadisticas_fase['puntos_local'] or 0) + (estadisticas_fase['puntos_visitante'] or 0),
            'faltas': (estadisticas_fase['faltas_local'] or 0) + (estadisticas_fase['faltas_visitante'] or 0),
            'rebotes': (estadisticas_fase['rebotes_local'] or 0) + (estadisticas_fase['rebotes_visitante'] or 0),
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



# Vista para mostrar el foro
def foro(request):
    return render(request, 'basquetbol/foro.html')




def bracket_eliminatorias(request, campeonato_id):
    # Obtener el campeonato y los partidos por fase
    campeonato = get_object_or_404(Campeonato, id=campeonato_id)
    partidos_cuartos = Partido.objects.filter(campeonato=campeonato, fase='Cuartos').order_by('fecha')
    partidos_semifinal = Partido.objects.filter(campeonato=campeonato, fase='Semifinal').order_by('fecha')
    partido_final = Partido.objects.filter(campeonato=campeonato, fase='Final').first()

    context = {
        'campeonato': campeonato,
        'partidos_cuartos': partidos_cuartos,
        'partidos_semifinal': partidos_semifinal,
        'partido_final': partido_final,
    }

    return render(request, 'basquetbol/bracket.html', context)



def estadisticas_equipos(request):
    equipos = Equipo.objects.annotate(
        total_puntos_local=Sum('partidos_local__estadisticas__puntos_equipo_local'),
        total_puntos_visitante=Sum('partidos_visitante__estadisticas__puntos_equipo_visitante'),
        total_triples_local=Sum('partidos_local__estadisticas__triples_equipo_local'),
        total_triples_visitante=Sum('partidos_visitante__estadisticas__triples_equipo_visitante'),
        total_pases_local=Sum('partidos_local__estadisticas__pases_equipo_local'),
        total_pases_visitante=Sum('partidos_visitante__estadisticas__pases_equipo_visitante'),
        total_rebotes_local=Sum('partidos_local__estadisticas__rebotes_equipo_local'),
        total_rebotes_visitante=Sum('partidos_visitante__estadisticas__rebotes_equipo_visitante'),
        total_faltas_local=Sum('partidos_local__estadisticas__faltas_equipo_local'),
        total_faltas_visitante=Sum('partidos_visitante__estadisticas__faltas_equipo_visitante'),
    ).annotate(
        total_puntos=F('total_puntos_local') + F('total_puntos_visitante'),
        total_triples=F('total_triples_local') + F('total_triples_visitante'),
        total_pases=F('total_pases_local') + F('total_pases_visitante'),
        total_rebotes=F('total_rebotes_local') + F('total_rebotes_visitante'),
        total_faltas=F('total_faltas_local') + F('total_faltas_visitante'),
    ).order_by('-total_puntos')

    return render(request, 'basquetbol/estadisticas_equipos.html', {
        'equipos': equipos,
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

def login_view(request):
    # Si el formulario se envía por POST
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)  # Iniciar sesión

            # Obtener el parámetro 'next' para redirigir al usuario a la página original que intentaba visitar
            next_url = request.GET.get('next', None)
            if next_url:
                return redirect(next_url)  # Redirigir al usuario a la URL original

            # Obtener un campeonato específico o el primero disponible
            campeonato = Campeonato.objects.first()  # Puedes ajustar esta lógica si necesitas un campeonato específico

            # Si no hay campeonatos, redirigir a la página de inicio o alguna página por defecto
            if not campeonato:
                campeonato = None  # O alguna lógica para redirigir a otra página

            # Redirigir según el tipo de usuario
            if user.is_superuser or user.groups.filter(name='Administrador').exists():
                return redirect('gestionar_registros')  # Redirigir a la vista para administrar registros
            elif user.groups.filter(name='Planillero').exists():
                # Si es planillero, redirigir a la lista de partidos del campeonato
                return redirect('lista_partidos', campeonato_id=campeonato.id if campeonato else None)
            else:
                # Para usuarios comunes, redirigir al próximo partido
                return redirect('proximo_partido')

        else:
            # Si las credenciales son incorrectas
            messages.error(request, "Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.")
    
    else:
        form = AuthenticationForm()  # Crear el formulario de autenticación vacío

    return render(request, 'basquetbol/login.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import RegistroForm

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            # Crear el usuario sin guardarlo aún en la base de datos
            user = form.save(commit=False)
            user.is_active = False  # Marcar al usuario como inactivo hasta que confirme su email
            user.save()

            # Enviar correo de confirmación
            send_confirmation_email(user, request)

            # Desloguear al usuario automáticamente, si estaba logueado
            logout(request)

            # Redirigir al login o mostrar un mensaje de éxito
            return render(request, 'basquetbol/success.html', {
                "message": "Registro exitoso. Por favor, verifica tu correo electrónico para activar tu cuenta."
            })
    else:
        form = RegistroForm()

    return render(request, 'basquetbol/registro.html', {'form': form})

#---------------------------CONFIRMACIÓN DE EMAIL------------------------------
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_text
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect

def confirmar_correo(request, uidb64, token):
    try:
        # Decodificar uid
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

        # Validar el token
        if default_token_generator.check_token(user, token):
            user.is_active = True  # Activar el usuario
            user.save()
            messages.success(request, '¡Cuenta activada exitosamente! Ahora puedes iniciar sesión.')
            return redirect('login')
        else:
            messages.error(request, 'El enlace de activación es inválido o ha expirado.')
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        messages.error(request, 'Hubo un error al intentar activar tu cuenta.')

    return redirect('login')

#-------------------- CONFIRMACIÓN DE EMAIL -------------------------
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

def send_confirmation_email(user, request):
    """Envía un correo de confirmación al usuario recién registrado."""
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))  # Codificar el ID del usuario

    # Crear URL para el enlace de confirmación dinámicamente
    current_site = get_current_site(request)
    activation_link = f"{request.scheme}://{current_site.domain}{reverse('activate', kwargs={'uidb64': uid, 'token': token})}"

    subject = 'Confirmación de Registro'
    message = (
        f"Hola {user.username},\n\n"
        f"Gracias por registrarte en nuestra plataforma. Por favor, confirma tu correo "
        f"haciendo clic en el siguiente enlace:\n\n{activation_link}\n\n"
        "Si no solicitaste esta cuenta, ignora este mensaje.\n\nSaludos,\nEquipo de Soporte."
    )
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]

    try:
        send_mail(subject, message, from_email, recipient_list)
        # Mensaje indicando que el correo de confirmación fue enviado
        messages.success(request, 'Registro exitoso. Te hemos enviado un correo de confirmación. Por favor, verifica tu bandeja de entrada.')
    except Exception as e:
        # Manejar errores en el envío del correo
        messages.error(request, f'Hubo un error al enviar el correo de confirmación: {str(e)}. Intenta más tarde.')

#---------------------------CONFIRMACIÓN DE EMAIL------------------------------

from django.shortcuts import redirect, render
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Tu cuenta ha sido activada exitosamente. Ahora puedes iniciar sesión.')
        return redirect('login')
    else:
        return render(request, 'activation_failed.html', {"message": "El enlace de activación no es válido."})


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
@login_required
@user_passes_test(lambda u: u.groups.filter(name='Planillero').exists())  # Asegúrate de que solo los planilleros puedan registrar estadísticas
def registrar_estadisticas_partido(request, partido_id):
    partido = get_object_or_404(Partido, id=partido_id)

    # Crear o recuperar las estadísticas del partido
    estadisticas, created = PartidoEstadistica.objects.get_or_create(partido=partido)

    if request.method == 'POST':
        form = PartidoStatsForm(request.POST, instance=estadisticas)
        if form.is_valid():
            form.save()

            # Actualizar posiciones después de registrar las estadísticas
            actualizar_posiciones(partido)

            messages.success(request, "Estadísticas del partido registradas exitosamente.")
            return redirect('lista_partidos', campeonato_id=partido.campeonato.id)
    else:
        form = PartidoStatsForm(instance=estadisticas)

    return render(request, 'basquetbol/registrar_estadisticas.html', {'form': form, 'partido': partido})




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








