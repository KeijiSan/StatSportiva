from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from .models import Equipo, Jugador, Entrenador, Campeonato
import datetime

# Formulario de registro de usuarios
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Formulario para el entrenador
class EntrenadorForm(forms.ModelForm):
    class Meta:
        model = Entrenador
        fields = ['nombre', 'nacionalidad', 'fecha_nacimiento']

    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
        if fecha_nacimiento and fecha_nacimiento > datetime.date.today():
            raise forms.ValidationError("La fecha de nacimiento no puede ser en el futuro.")
        return fecha_nacimiento


# Formulario para inscribir un equipo
class InscripcionEquipoForm(forms.ModelForm):
    fundacion = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False
    )
    color_principal = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))
    color_secundario = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))

    class Meta:
        model = Equipo
        fields = ['nombre', 'campeonato', 'fundacion', 'historia', 'color_principal', 'color_secundario', 'logo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Añadir una opción vacía para que ningún campeonato esté seleccionado por defecto
        campeonatos = Campeonato.objects.all()
        choices = [('', 'Seleccione un campeonato')]  # Opción vacía

        for campeonato in campeonatos:
            if campeonato.equipos.count() >= campeonato.max_equipos:
                choices.append((campeonato.id, f"{campeonato.nombre} (Lleno)"))
            else:
                choices.append((campeonato.id, campeonato.nombre))

        # Sobrescribir el campo campeonato para usar estas opciones
        self.fields['campeonato'].choices = choices

        # Mantener la fecha de fundación si ya existe
        if self.instance.pk and self.instance.fundacion:
            self.fields['fundacion'].initial = self.instance.fundacion

    def clean_fundacion(self):
        fundacion = self.cleaned_data.get('fundacion')
        if fundacion and fundacion > datetime.date.today():
            raise forms.ValidationError('La fecha de fundación no puede ser en el futuro.')
        return fundacion

    def clean(self):
        cleaned_data = super().clean()
        campeonato = cleaned_data.get('campeonato')

        if campeonato and campeonato.equipos.count() >= campeonato.max_equipos:
            raise forms.ValidationError(f'Este campeonato ya ha alcanzado el máximo de {campeonato.max_equipos} equipos inscritos.')

        return cleaned_data


# Formulario para crear un campeonato
class CrearCampeonatoForm(forms.ModelForm):
    class Meta:
        model = Campeonato
        fields = ['nombre', 'fecha_inicio', 'fecha_fin', 'descripcion', 'max_equipos', 'premios']

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')

        if fecha_inicio and fecha_fin and fecha_fin < fecha_inicio:
            raise forms.ValidationError('La fecha de fin no puede ser anterior a la fecha de inicio.')

        return cleaned_data


# Formulario individual para el modelo Jugador
class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['nombre', 'posicion', 'numero']

    def clean_numero(self):
        numero = self.cleaned_data.get('numero')
        equipo = self.instance.equipo
        if equipo and equipo.jugadores.filter(numero=numero).exists():
            raise forms.ValidationError(f"El número {numero} ya está asignado a otro jugador en este equipo.")
        return numero


# Crear el formset para gestionar múltiples instancias del modelo Jugador asociado a un equipo
JugadorFormSet = inlineformset_factory(
    Equipo,  # Modelo al que se vincula (Equipo)
    Jugador,  # Modelo que se va a gestionar en el formset (Jugador)
    form=JugadorForm,  # El formulario base para cada jugador
    extra=1,  # Número de formularios vacíos por defecto para agregar nuevos jugadores
    can_delete=True,  # Permitir eliminación de jugadores existentes
    min_num=5,  # Mínimo de jugadores requeridos
    max_num=9,  # Máximo de jugadores permitidos
    validate_min=True,  # Validar que se cumpla el mínimo de jugadores
    validate_max=True  # Validar que no se exceda el máximo de jugadores
)
