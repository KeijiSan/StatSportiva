from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .forms import InscripcionEquipoForm, EntrenadorForm, JugadorFormSet, CrearCampeonatoForm, RegistroForm
from .models import Equipo, Jugador, Entrenador, Campeonato


# Vista para mostrar el próximo partido
def proximo_partido(request):
    equipo_inscrito = (
        Equipo.objects.filter(entrenador__user=request.user).exists()
        if request.user.is_authenticated
        else False
    )
    return render(request, 'basquetbol/proximo_partido.html', {'equipo_inscrito': equipo_inscrito})


# Vista para inscribir un equipo en un campeonato
@login_required
def inscribir_equipo(request):
    if request.method == 'POST':
        equipo_form = InscripcionEquipoForm(request.POST, request.FILES)
        entrenador_form = EntrenadorForm(request.POST)
        jugador_formset = JugadorFormSet(request.POST)

        if equipo_form.is_valid() and entrenador_form.is_valid() and jugador_formset.is_valid():
            entrenador = entrenador_form.save(commit=False)
            entrenador.user = request.user
            entrenador.save()

            equipo = equipo_form.save(commit=False)
            equipo.entrenador = entrenador
            equipo.save()

            jugadores = jugador_formset.save(commit=False)
            for jugador in jugadores:
                jugador.equipo = equipo
                jugador.save()

            messages.success(request, "¡Equipo inscrito exitosamente!")
            return redirect('proximo_partido')
        else:
            messages.error(request, "Hubo un error al inscribir el equipo.")
    else:
        equipo_form = InscripcionEquipoForm()
        entrenador_form = EntrenadorForm()
        jugador_formset = JugadorFormSet()

    return render(request, 'basquetbol/inscribir_equipo.html', {
        'equipo_form': equipo_form,
        'entrenador_form': entrenador_form,
        'jugador_formset': jugador_formset
    })


# Vista para listar todos los campeonatos
def lista_campeonatos(request):
    campeonatos = Campeonato.objects.all()
    return render(request, 'basquetbol/lista_campeonatos.html', {'campeonatos': campeonatos})


# Vista para crear un nuevo campeonato
@login_required
def crear_campeonato(request):
    if request.method == 'POST':
        form = CrearCampeonatoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Campeonato creado exitosamente.")
            return redirect('lista_campeonatos')
        else:
            messages.error(request, "Hubo un error al crear el campeonato.")
    else:
        form = CrearCampeonatoForm()

    return render(request, 'basquetbol/crear_campeonato.html', {'form': form})


# Vista para registrar un nuevo usuario
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Tu cuenta ha sido creada exitosamente! Ahora puedes iniciar sesión.")
            return redirect('login')
        else:
            messages.error(request, "Hubo un error al registrar tu cuenta. Por favor, inténtalo nuevamente.")
    else:
        form = RegistroForm()

    return render(request, 'basquetbol/registro.html', {'form': form})


# Vista para mostrar los detalles de un campeonato específico
def detalle_campeonato(request, campeonato_id):
    campeonato = get_object_or_404(Campeonato, id=campeonato_id)
    equipos = campeonato.equipos.all()
    return render(request, 'basquetbol/detalle_campeonato.html', {'campeonato': campeonato, 'equipos': equipos})


# Vista para gestionar el perfil de usuario, permitiendo modificar equipo y jugadores
@login_required
def perfil_usuario(request):
    try:
        entrenador = Entrenador.objects.get(user=request.user)
    except Entrenador.DoesNotExist:
        return redirect('inscribir_equipo')

    equipo = get_object_or_404(Equipo, entrenador=entrenador)
    jugadores = equipo.jugadores.all()

    if request.method == 'POST':
        equipo_form = InscripcionEquipoForm(request.POST, request.FILES, instance=equipo)
        jugador_formset = JugadorFormSet(request.POST, instance=equipo)

        if equipo_form.is_valid() and jugador_formset.is_valid():
            equipo_form.save()
            jugador_formset.save()
            messages.success(request, "Cambios guardados exitosamente.")
            return redirect('perfil_usuario')
        else:
            messages.error(request, "Error al guardar los cambios.")
    else:
        equipo_form = InscripcionEquipoForm(instance=equipo)
        jugador_formset = JugadorFormSet(instance=equipo)

    return render(request, 'basquetbol/perfil_usuario.html', {
        'equipo_form': equipo_form,
        'jugador_formset': jugador_formset,
        'equipo': equipo,
        'jugadores': jugadores,
    })


# Vista para abandonar el campeonato, eliminando el equipo y el entrenador
@login_required
def abandonar_campeonato(request):
    try:
        equipo = get_object_or_404(Equipo, entrenador__user=request.user)
        entrenador = get_object_or_404(Entrenador, user=request.user)

        if request.method == 'POST':
            equipo.delete()
            entrenador.delete()
            messages.success(request, "Has abandonado el campeonato exitosamente.")
            return redirect('perfil_usuario')
    except Exception as e:
        messages.error(request, f"Ocurrió un error: {str(e)}")

    return render(request, 'basquetbol/abandonar_campeonato.html', {'equipo': equipo})


# Vista para mostrar el foro
def foro(request):
    return render(request, 'basquetbol/foro.html')


# Vista para la Política de Privacidad
def politica_privacidad(request):
    return render(request, 'basquetbol/politica_privacidad.html')

from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render

def login_view(request):
    form = AuthenticationForm(request)
    return render(request, 'basquetbol/login.html', {'form': form})
