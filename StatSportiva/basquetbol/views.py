from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import InscripcionEquipoForm, EntrenadorForm, JugadorFormSet, CrearCampeonatoForm, RegistroForm
from .models import Equipo, Jugador, Entrenador, Campeonato


# Vista para mostrar el próximo partido
def proximo_partido(request):
    # Verifica si el usuario tiene un equipo inscrito
    equipo_inscrito = Equipo.objects.filter(entrenador__user=request.user).exists() if request.user.is_authenticated else False
    return render(request, 'basquetbol/proximo_partido.html', {'equipo_inscrito': equipo_inscrito})
def lista_campeonatos(request):
    campeonatos = Campeonato.objects.all()
    return render(request, 'basquetbol/lista_campeonatos.html', {'campeonatos': campeonatos})


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
            entrenador.user = request.user
            entrenador.save()

            # Crear un nuevo equipo asociado al entrenador
            equipo = equipo_form.save(commit=False)
            equipo.entrenador = entrenador
            equipo.save()

            # Guardar los jugadores asociados al equipo
            jugadores = jugador_formset.save(commit=False)
            for jugador in jugadores:
                jugador.equipo = equipo
                jugador.save()

            return redirect('proximo_partido')
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


# Vista para listar todos los campeonatos
def lista_campeonatos(request):
    campeonatos = Campeonato.objects.all()
    return render(request, 'basquetbol/lista_campeonatos.html', {'campeonatos': campeonatos})


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


# Vista para registrar un nuevo usuario
from django.contrib.auth import login
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Iniciar sesión automáticamente
            return redirect('proximo_partido')
    else:
        form = RegistroForm()

    return render(request, 'basquetbol/registro.html', {'form': form})


# Vista para mostrar los detalles de un campeonato específico
def detalle_campeonato(request, campeonato_id):
    campeonato = Campeonato.objects.get(id=campeonato_id)
    equipos = campeonato.equipos.all()
    return render(request, 'basquetbol/detalle_campeonato.html', {'campeonato': campeonato, 'equipos': equipos})


# Vista para gestionar el perfil de usuario, permitiendo modificar equipo y jugadores
@login_required
def perfil_usuario(request):
    # Intentar obtener el entrenador asociado al usuario
    try:
        entrenador = Entrenador.objects.get(user=request.user)
    except Entrenador.DoesNotExist:
        # Si no existe, redirigir a la inscripción de equipo
        return redirect('inscribir_equipo')

    # Obtener el equipo asociado al entrenador
    equipo = get_object_or_404(Equipo, entrenador=entrenador)
    jugadores = equipo.jugadores.all()

    if request.method == 'POST':
        equipo_form = InscripcionEquipoForm(request.POST, request.FILES, instance=equipo)
        jugador_formset = JugadorFormSet(request.POST, instance=equipo)

        if equipo_form.is_valid() and jugador_formset.is_valid():
            equipo = equipo_form.save(commit=False)
            equipo.save()

            jugadores = jugador_formset.save(commit=False)
            for jugador in jugadores:
                jugador.equipo = equipo
                jugador.save()

            # Guardar todas las relaciones del formset
            jugador_formset.save_m2m()

            messages.success(request, "Cambios guardados exitosamente")
            return redirect('perfil_usuario')
        else:
            messages.error(request, "Error al guardar los cambios")
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
    # Obtener el equipo asociado al entrenador del usuario
    equipo = get_object_or_404(Equipo, entrenador__user=request.user)

    if request.method == 'POST':
        # Eliminar el equipo y el entrenador asociado al usuario
        equipo.delete()
        entrenador = get_object_or_404(Entrenador, user=request.user)
        entrenador.delete()

        return redirect('perfil_usuario')

    return render(request, 'basquetbol/abandonar_campeonato.html', {'equipo': equipo})

# Vista para mostrar el foro
def foro(request):
    return render(request, 'basquetbol/foro.html')
