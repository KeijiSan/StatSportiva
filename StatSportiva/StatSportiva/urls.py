from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from basquetbol import views
from django.urls import path, include
from basquetbol.views import confirmar_correo


urlpatterns = [
    #------------------ KEIJI---------------------------------
    path('', views.proximo_partido, name='vista_principal'),  # Página principal
    path('logout/', auth_views.LogoutView.as_view(next_page='vista_principal'), name='logout'),  # Logout redirige a la página principal
    path('politica-privacidad/', views.politica_privacidad, name='politica_privacidad'),  # Política de privacidad
    path('accounts/', include('allauth.urls')),  # Rutas de django-allauth
    path('nosotros/', views.nosotros, name='nosotros'),

    #----------------------------- olvido password -----------------------------
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='basquetbol/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='basquetbol/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='basquetbol/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='basquetbol/password_reset_complete.html'), name='password_reset_complete'),
 
    # -------------------------- Admin --------------------------
    path('admin/', admin.site.urls),
    path('api/estadisticas-equipo/<int:equipo_id>/', views.estadisticas_equipo_api, name='estadisticas_equipo_api'),
    
    # -------------------------- Autenticación --------------------------
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro, name='registro'),
    path('confirmar/<uidb64>/<token>/', views.confirmar_correo, name='confirmar_correo'),
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
    # -------------------------- Foro --------------------------
    path('foro/', views.foro, name='foro'),
    path('like/', views.like_publicacion, name='like_publicacion'),
    path('comentar/', views.agregar_comentario, name='agregar_comentario'),
    path("agregar_comentario/", views.agregar_comentario, name="agregar_comentario"),
    path('eliminar-publicacion/<int:publicacion_id>/', views.eliminar_publicacion, name='eliminar_publicacion'),
    path('eliminar-comentario/<int:comentario_id>/', views.eliminar_comentario, name='eliminar_comentario'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
