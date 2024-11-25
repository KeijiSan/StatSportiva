from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from basquetbol import views
from django.urls import path, include
from basquetbol.views import create_post,like_post,delete_post


urlpatterns = [
    #------------------ KEIJI---------------------------------
    path('', views.proximo_partido, name='vista_principal'),  # Página principal
    path('logout/', auth_views.LogoutView.as_view(next_page='vista_principal'), name='logout'),
    path('politica-privacidad/', views.politica_privacidad, name='politica_privacidad'),  # Política de privacidad
    path('accounts/', include('allauth.urls')),  # Rutas de django-allauth
    path('nosotros/', views.nosotros, name='nosotros'),
    
    
    path('foro/', views.foro, name='foro'),
    path('create/', views.create_post, name='create_post'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('reply/<int:post_id>/', views.reply_post, name='reply_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),  # Ruta para eliminar un post
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # Ruta para cerrar sesión

    # -------------------------- Admin --------------------------
    path('admin/', admin.site.urls),

    # -------------------------- Autenticación --------------------------
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('registro/', views.registro, name='registro'),

    # -------------------------- Perfil de Usuario --------------------------
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('abandonar_campeonato/', views.abandonar_campeonato, name='abandonar_campeonato'),

    # -------------------------- Gestión de Campeonatos --------------------------
    path('gestionar_registros/', views.gestionar_registros, name='gestionar_registros'),
    path('campeonatos/', views.lista_campeonatos, name='lista_campeonatos'),
    path('crear_campeonato/', views.crear_campeonato, name='crear_campeonato'),
    path('campeonato/<int:campeonato_id>/', views.detalle_campeonato, name='detalle_campeonato'),
    path('campeonato/<int:campeonato_id>/generar_partidos/', views.generar_partidos_clasificatorias_view, name='generar_partidos_clasificatorias'),
    path('campeonatos/<int:campeonato_id>/octavos/', views.octavos_view, name='octavos_view'),
    path('campeonatos/<int:campeonato_id>/generar_fase_eliminatoria/', views.generar_fase_eliminatoria, name='generar_fase_eliminatoria'),
    path('campeonatos/<int:campeonato_id>/bracket/', views.bracket_eliminatorias, name='bracket_eliminatorias'),
    path('tabla_posiciones/', views.tabla_posiciones, name='tabla_posiciones'),

    # -------------------------- Equipos --------------------------
    path('inscribir_equipo/', views.inscribir_equipo, name='inscribir_equipo'),
    path('estadisticas-equipos/', views.estadisticas_equipos, name='estadisticas_equipos'),

    # -------------------------- Partidos --------------------------
    path('proximo_partido/', views.proximo_partido, name='proximo_partido'),
    path('partidos/', views.lista_partidos, name='lista_partidos'),
    path('partidos/<int:campeonato_id>/', views.lista_partidos, name='lista_partidos'),
    path('seleccionar-partido/', views.seleccionar_partido, name='seleccionar_partido'),
    path('partido/<int:partido_id>/registrar_estadisticas/', views.registrar_estadisticas_partido, name='registrar_estadisticas_partido'),
    path('partido/<int:partido_id>/registrar-estadisticas/', views.registrar_estadisticas_partido, name='registrar_estadisticas'),

    # -------------------------- Utilidades --------------------------
    path('buscar/', views.buscar_partidos, name='buscar_partidos'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
