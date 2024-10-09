from pyexpat.errors import messages
from django.shortcuts import render, redirect
from .forms import InscripcionEquipoForm, EntrenadorForm, JugadorForm, JugadorFormSet
from .models import Campeonato, Equipo, Entrenador
from django.forms import inlineformset_factory
from django.contrib import messages


from django.shortcuts import render

def proximo_partido(request):
    equipo_inscrito = Equipo.objects.filter(entrenador__user=request.user).exists() if request.user.is_authenticated else False
    return render(request, 'basquetbol/proximo_partido.html', {'equipo_inscrito': equipo_inscrito})



from django.contrib.auth.decorators import login_required

@login_required
def inscribir_equipo(request):
    if request.method == 'POST':
        equipo_form = InscripcionEquipoForm(request.POST, request.FILES)
        entrenador_form = EntrenadorForm(request.POST)
        jugador_formset = JugadorFormSet(request.POST)

        if equipo_form.is_valid() and entrenador_form.is_valid() and jugador_formset.is_valid():
            # Crear el entrenador y asociarlo con el usuario autenticado
            entrenador = entrenador_form.save(commit=False)
            entrenador.user = request.user
            entrenador.save()

            # Crear el equipo y asociarlo con el entrenador recién creado
            equipo = equipo_form.save(commit=False)
            equipo.entrenador = entrenador
            equipo.save()

            # Guardar los jugadores asociados al equipo
            jugadores = jugador_formset.save(commit=False)
            for jugador in jugadores:
                jugador.equipo = equipo
                jugador.save()

            return redirect('proximo_partido')  # Redirige a la página que desees
    else:
        equipo_form = InscripcionEquipoForm()
        entrenador_form = EntrenadorForm()
        jugador_formset = JugadorFormSet()

    return render(request, 'basquetbol/inscribir_equipo.html', {
        'equipo_form': equipo_form,
        'entrenador_form': entrenador_form,
        'jugador_formset': jugador_formset
    })


def lista_campeonatos(request):
    campeonatos = Campeonato.objects.all()
    return render(request, 'basquetbol/lista_campeonatos.html', {'campeonatos': campeonatos})




from django.shortcuts import render, redirect
from .forms import CrearCampeonatoForm

def crear_campeonato(request):
    if request.method == 'POST':
        form = CrearCampeonatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_campeonatos')  # Redirige a la lista de campeonatos
        else:
            # Si el formulario no es válido, imprime los errores en la terminal (solo para depuración)
            print("Errores en el formulario: ", form.errors)
    else:
        form = CrearCampeonatoForm()

    return render(request, 'basquetbol/crear_campeonato.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistroForm

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente después de registrarse
            return redirect('lista_campeonatos')  # Redirige a la lista de campeonatos después de registrarse
    else:
        form = RegistroForm()

    return render(request, 'basquetbol/registro.html', {'form': form})


def detalle_campeonato(request, campeonato_id):
    campeonato = Campeonato.objects.get(id=campeonato_id)
    equipos = campeonato.equipos.all()  # Accedemos a los equipos de ese campeonato

    return render(request, 'basquetbol/detalle_campeonato.html', {'campeonato': campeonato, 'equipos': equipos})



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Equipo, Jugador
from .forms import InscripcionEquipoForm, JugadorFormSet, EntrenadorForm


@login_required
def perfil_usuario(request):
    # Verificar si el usuario tiene un entrenador asociado
    try:
        entrenador = Entrenador.objects.get(user=request.user)
    except Entrenador.DoesNotExist:
        # Si no tiene un entrenador, redirigir a la página de creación de equipo
        return redirect('inscribir_equipo')

    # Obtener el equipo del entrenador
    equipo = get_object_or_404(Equipo, entrenador=entrenador)
    jugadores = equipo.jugadores.all()

    if request.method == 'POST':
        equipo_form = InscripcionEquipoForm(request.POST, request.FILES, instance=equipo)
        jugador_formset = JugadorFormSet(request.POST, instance=equipo)

        if equipo_form.is_valid() and jugador_formset.is_valid():
            equipo_form.save()  # Guardar el equipo
            
            # Guardar el formset de jugadores sin comprometerlos aún
            jugadores = jugador_formset.save(commit=False)

            # Asociar cada jugador con el equipo y guardarlos
            for jugador in jugadores:
                jugador.equipo = equipo
                jugador.save()

            # Guardar el formset completo (esto incluye relaciones como M2M si existen)
            jugador_formset.save_m2m()

            return redirect('perfil_usuario')  # Redirigir al perfil del usuario
        else:
            # Si hay errores, imprimirlos para depuración
            print(jugador_formset.errors)
    else:
        equipo_form = InscripcionEquipoForm(instance=equipo)
        jugador_formset = JugadorFormSet(instance=equipo)

    return render(request, 'basquetbol/perfil_usuario.html', {
        'equipo_form': equipo_form,
        'jugador_formset': jugador_formset,
        'equipo': equipo,
        'jugadores': jugadores,
    })


    
    

@login_required
def abandonar_campeonato(request):
    # Obtener el equipo asociado al entrenador del usuario
    equipo = get_object_or_404(Equipo, entrenador__user=request.user)

    if request.method == 'POST':
        # Eliminar el equipo
        equipo.delete()
        
        # Eliminar el entrenador asociado al usuario
        entrenador = get_object_or_404(Entrenador, user=request.user)
        entrenador.delete()

        # Redirigir al perfil después de eliminar
        return redirect('perfil_usuario')

    return render(request, 'basquetbol/abandonar_campeonato.html', {'equipo': equipo})



