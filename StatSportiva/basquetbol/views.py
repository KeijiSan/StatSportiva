from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import InscripcionEquipoForm, EntrenadorForm, JugadorFormSet, CrearCampeonatoForm, PartidoForm, ComentarioForm, RegistroForm
from .models import Equipo, Jugador, Entrenador, Campeonato, Partido, Tema, Comentario, Clasificacion


# Vista para mostrar el próximo partido
def proximo_partido(request):
    equipo_inscrito = Equipo.objects.filter(entrenador__user=request.user).exists() if request.user.is_authenticated else False
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

            return redirect('proximo_partido')
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
def crear_campeonato(request):
    if request.method == 'POST':
        form = CrearCampeonatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_campeonatos')
        else:
            print("Errores en el formulario: ", form.errors)
    else:
        form = CrearCampeonatoForm()

    return render(request, 'basquetbol/crear_campeonato.html', {'form': form})


# Vista para gestionar los partidos de un campeonato
@login_required
def gestionar_partido(request, partido_id):
    partido = get_object_or_404(Partido, id=partido_id)
    if request.method == 'POST':
        form = PartidoForm(request.POST, instance=partido)
        if form.is_valid():
            form.save()
            messages.success(request, "Partido actualizado con éxito")
            return redirect('calendario_partidos', campeonato_id=partido.campeonato.id)
    else:
        form = PartidoForm(instance=partido)

    return render(request, 'basquetbol/gestionar_partido.html', {'form': form, 'partido': partido})


# Vista para ver el calendario de partidos
def calendario_partidos(request, campeonato_id):
    campeonato = get_object_or_404(Campeonato, id=campeonato_id)
    partidos = campeonato.partidos.all().order_by('fecha')
    return render(request, 'basquetbol/calendario_partidos.html', {'campeonato': campeonato, 'partidos': partidos})


# Vista para registrar un nuevo usuario
from django.contrib.auth import login
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('lista_campeonatos')
    else:
        form = RegistroForm()

    return render(request, 'basquetbol/registro.html', {'form': form})


# Vista para mostrar los detalles de un campeonato específico
def detalle_campeonato(request, campeonato_id):
    campeonato = Campeonato.objects.get(id=campeonato_id)
    equipos = campeonato.equipos.all()
    return render(request, 'basquetbol/detalle_campeonato.html', {'campeonato': campeonato, 'equipos': equipos})


# Vista para gestionar el perfil de usuario
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
            equipo = equipo_form.save(commit=False)
            equipo.save()

            jugadores = jugador_formset.save(commit=False)
            for jugador in jugadores:
                jugador.equipo = equipo
                jugador.save()

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


# Vista para abandonar el campeonato
@login_required
def abandonar_campeonato(request):
    equipo = get_object_or_404(Equipo, entrenador__user=request.user)

    if request.method == 'POST':
        equipo.delete()
        entrenador = get_object_or_404(Entrenador, user=request.user)
        entrenador.delete()

        return redirect('perfil_usuario')

    return render(request, 'basquetbol/abandonar_campeonato.html', {'equipo': equipo})


# Vista para el foro y gestión de temas y comentarios
def foro(request):
    temas = Tema.objects.all()
    return render(request, 'basquetbol/foro.html', {'temas': temas})


def foro_tema(request, tema_id):
    tema = get_object_or_404(Tema, id=tema_id)
    comentarios = tema.comentarios.all()

    if request.method == 'POST':
        comentario_form = ComentarioForm(request.POST)
        if comentario_form.is_valid():
            comentario = comentario_form.save(commit=False)
            comentario.autor = request.user
            comentario.tema = tema
            comentario.save()
            return redirect('foro_tema', tema_id=tema.id)
    else:
        comentario_form = ComentarioForm()

    return render(request, 'basquetbol/foro_tema.html', {
        'tema': tema,
        'comentarios': comentarios,
        'comentario_form': comentario_form,
    })


# Vista para el historial de un equipo
@login_required
def historial_equipo(request):
    entrenador = get_object_or_404(Entrenador, user=request.user)
    equipo = get_object_or_404(Equipo, entrenador=entrenador)
    partidos_local = equipo.partidos_local.all()
    partidos_visitante = equipo.partidos_visitante.all()

    return render(request, 'basquetbol/historial_equipo.html', {
        'equipo': equipo,
        'partidos_local': partidos_local,
        'partidos_visitante': partidos_visitante,
    })


# Vista para ver la clasificación del campeonato
def clasificacion(request, campeonato_id):
    campeonato = get_object_or_404(Campeonato, id=campeonato_id)
    clasificaciones = Clasificacion.objects.filter(equipo__campeonato=campeonato).order_by('-puntos')
    return render(request, 'basquetbol/clasificacion.html', {'clasificaciones': clasificaciones})
