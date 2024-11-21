from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from basquetbol import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.proximo_partido, name='vista_principal'),  # Página principal
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('foro/', views.foro, name='foro'),
    path('abandonar_campeonato/', views.abandonar_campeonato, name='abandonar_campeonato'),
    path('proximo_partido/', views.proximo_partido, name='proximo_partido'),
    path('inscribir_equipo/', views.inscribir_equipo, name='inscribir_equipo'),
    path('campeonatos/', views.lista_campeonatos, name='lista_campeonatos'),
    path('crear_campeonato/', views.crear_campeonato, name='crear_campeonato'),
    path('login/', auth_views.LoginView.as_view(template_name='basquetbol/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='vista_principal'), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('campeonato/<int:campeonato_id>/', views.detalle_campeonato, name='detalle_campeonato'),
    path('politica-privacidad/', views.politica_privacidad, name='politica_privacidad'),  # Política de privacidad
    path('accounts/', include('allauth.urls')),  # Rutas de django-allauth
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
