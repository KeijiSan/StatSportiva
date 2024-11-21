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

    def clean_fundacion(self):
        fundacion = self.cleaned_data.get('fundacion')
        if fundacion and fundacion > datetime.date.today():
            raise forms.ValidationError('La fecha de fundación no puede ser en el futuro.')
        return fundacion

    def clean_color_principal(self):
        color = self.cleaned_data.get('color_principal')
        if not color.startswith('#') or len(color) != 7:
            raise forms.ValidationError("El color principal debe ser un código hexadecimal válido (e.g., #FFFFFF).")
        return color

    def clean(self):
        cleaned_data = super().clean()
        campeonato = cleaned_data.get('campeonato')

        if campeonato and campeonato.equipos.count() >= campeonato.max_equipos:
            raise forms.ValidationError(f'Este campeonato ya tiene el máximo de {campeonato.max_equipos} equipos inscritos.')

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


# Formset para gestionar múltiples jugadores
JugadorFormSet = inlineformset_factory(
    Equipo,
    Jugador,
    form=JugadorForm,
    extra=1,
    can_delete=True
)
