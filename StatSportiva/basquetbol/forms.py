from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from .models import Equipo, Jugador, Entrenador, Campeonato, PartidoEstadistica
import datetime

# Formulario de registro de usuarios
# Este formulario extiende el formulario de creación de usuarios de Django e incluye un campo de correo electrónico requerido.
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Campos que se incluirán en el formulario


# Formulario para el entrenador
# Utilizado para crear o editar la información del entrenador asociado a un equipo.
from django import forms
from .models import Entrenador

class EntrenadorForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Fecha de Nacimiento"
    )

    class Meta:
        model = Entrenador
        fields = ['nombre_entrenador', 'nacionalidad', 'fecha_nacimiento']


# Formulario para inscribir un equipo
# Permite gestionar la inscripción de un equipo en un campeonato, incluyendo la información del equipo y los colores.
class InscripcionEquipoForm(forms.ModelForm):
    fundacion = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False  # Hacer que el campo sea opcional para evitar errores al modificar un equipo existente
    )

    color_principal = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))
    color_secundario = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))

    class Meta:
        model = Equipo
        fields = ['nombre_equipo', 'campeonato', 'fundacion', 'historia', 'color_principal', 'color_secundario', 'logo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Añadir una opción vacía para que ningún campeonato esté seleccionado por defecto
        campeonatos = Campeonato.objects.all()
        choices = [('', 'Seleccione un campeonato')]

        for campeonato in campeonatos:
            if campeonato.equipos.count() >= campeonato.max_equipos:
                choices.append((campeonato.id, f"{campeonato.nombre} (Lleno)"))
            else:
                choices.append((campeonato.id, campeonato.nombre))

        # Sobrescribir el campo campeonato para usar estas opciones
        self.fields['campeonato'].choices = choices

        # Si estamos modificando, hacer que el campeonato sea de solo lectura
        if self.instance.pk:
            self.fields['campeonato'].widget.attrs['disabled'] = True

    def clean(self):
        cleaned_data = super().clean()
        campeonato = cleaned_data.get('campeonato')

        # Validar el número máximo de equipos inscritos solo si estamos creando un equipo nuevo
        if not self.instance.pk and campeonato and campeonato.equipos.count() >= campeonato.max_equipos:
            raise forms.ValidationError(f'Este campeonato ya ha alcanzado el máximo de {campeonato.max_equipos} equipos inscritos.')

        return cleaned_data

    def save(self, commit=True):
        # Si el campo 'campeonato' está deshabilitado, debemos ignorarlo al guardar
        if self.instance.pk:
            self.cleaned_data.pop('campeonato', None)
        return super().save(commit=commit)


# Formulario para crear un campeonato
# Permite gestionar la creación y edición de campeonatos, incluyendo fechas y detalles del campeonato.
class CrearCampeonatoForm(forms.ModelForm):
    class Meta:
        model = Campeonato
        # Especifica los campos del modelo Campeonato que se incluirán en el formulario
        fields = ['nombre', 'fecha_inicio', 'fecha_fin', 'descripcion', 'max_equipos', 'premios']

    # Validación personalizada para comprobar que la fecha de fin no sea anterior a la fecha de inicio
    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')

        if fecha_inicio and fecha_fin and fecha_fin < fecha_inicio:
            raise forms.ValidationError('La fecha de fin no puede ser anterior a la fecha de inicio.')

        return cleaned_data


# forms.py
from django import forms
from .models import Jugador

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['nombre', 'posicion', 'numero']  # Campos del modelo Jugador a incluir en el formulario
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'posicion': forms.Select(attrs={'class': 'form-control'}),  # Lista desplegable
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
        }



# Crear el formset para gestionar múltiples instancias del modelo Jugador asociado a un equipo
# forms.py (continuación)
from django.forms import inlineformset_factory
from .models import Equipo, Jugador

# Formset para gestionar los jugadores
JugadorFormSet = inlineformset_factory(
    Equipo,  # Modelo al que se vincula (Equipo)
    Jugador,  # Modelo que se va a gestionar en el formset (Jugador)
    form=JugadorForm,  # El formulario actualizado para cada jugador
    extra=1,
    can_delete=True,
    min_num=5,
    max_num=9,
    validate_min=True,
    validate_max=True
)



# Formulario para registrar estadísticas del partido
class PartidoStatsForm(forms.ModelForm):
    class Meta:
        model = PartidoEstadistica
        fields = [
            'pases_equipo_local',
            'pases_equipo_visitante',
            'faltas_equipo_local',
            'faltas_equipo_visitante',
            'triples_equipo_local',
            'triples_equipo_visitante',
            'rebotes_equipo_local',
            'rebotes_equipo_visitante',
            'puntos_equipo_local',  # Añadir puntos del equipo local
            'puntos_equipo_visitante',  # Añadir puntos del equipo visitante
        ]
