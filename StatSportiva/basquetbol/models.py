from django.db import models
from django.contrib.auth.models import User




# Modelo Fase
class Fase(models.Model):
    """
    Representa una fase dentro de un campeonato. Cada fase está asociada a un campeonato y tiene un orden específico.
    """
    nombre = models.CharField(max_length=100)
    campeonato = models.ForeignKey('Campeonato', related_name='fases', on_delete=models.CASCADE)
    orden = models.PositiveIntegerField(help_text="Orden de la fase en el campeonato (1 para la fase inicial, etc.)")

    def __str__(self):
        return f"{self.nombre} - {self.campeonato.nombre}"





# Modelo Campeonato
class Campeonato(models.Model):
    nombre = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.TextField()
    max_equipos = models.PositiveIntegerField(default=10)
    premios = models.CharField(max_length=255, null=True, blank=True)



    def __str__(self):
        return self.nombre




    def equipo_count(self):
        return self.equipos.count()




    def calcular_puntos(self):
        equipos = Equipo.objects.filter(campeonato=self)
        puntos = {equipo: 0 for equipo in equipos}
        partidos = Partido.objects.filter(fase='Clasificatorias', equipo_local__in=equipos)

        for partido in partidos:
            if partido.goles_local is not None and partido.goles_visitante is not None:
                if partido.goles_local > partido.goles_visitante:
                    puntos[partido.equipo_local] += 3
                elif partido.goles_local < partido.goles_visitante:
                    puntos[partido.equipo_visitante] += 3
                else:
                    puntos[partido.equipo_local] += 1
                    puntos[partido.equipo_visitante] += 1

        equipos_ordenados = sorted(puntos.keys(), key=lambda e: puntos[e], reverse=True)
        equipos_clasificados = equipos_ordenados[:8]
        equipos_eliminados = equipos_ordenados[-2:]
        return equipos_clasificados, equipos_eliminados






# Modelo Estadio
class Estadio(models.Model):
    """
    Representa un estadio donde se realizan los partidos, con nombre, capacidad y ciudad.
    """
    nombre = models.CharField(max_length=100)
    capacidad = models.PositiveIntegerField()
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre





# Modelo Entrenador
class Entrenador(models.Model):
    """
    Representa a un entrenador asociado a un usuario, con su información personal.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre_entrenador = models.CharField(max_length=100)  # Cambiado de 'nombre' a 'nombre_entrenador' para evitar conflicto
    nacionalidad = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nombre_entrenador






# Modelo Equipo
class Equipo(models.Model):
    """
    Representa a un equipo en un campeonato, con información sobre el equipo y su entrenador.
    """
    nombre_equipo = models.CharField(max_length=100)  # Cambiado de 'nombre' a 'nombre_equipo' para evitar conflicto con entrenador
    historia = models.TextField(null=True, blank=True)
    color_principal = models.CharField(max_length=7)
    color_secundario = models.CharField(max_length=7)
    logo = models.ImageField(upload_to='logos_equipos/', null=True, blank=True, default='logos_equipos/default_logo.png')
    sitio_web = models.URLField(max_length=200, null=True, blank=True)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE, related_name='equipos', null=True, blank=True)
    entrenador = models.OneToOneField('Entrenador', on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)  # Indica si el equipo está activo o eliminado
    campeon = models.ForeignKey('Equipo', on_delete=models.SET_NULL, null=True, blank=True)  # Referencia correcta usando cadena de texto

    def __str__(self):
        return self.nombre_equipo





# Modelo Jugador
class Jugador(models.Model):
    """
    Representa a un jugador en un equipo, con nombre, posición, número y equipo al que pertenece.
    """
    POSICIONES = [
        ('BASE', 'Base'),
        ('ESCOLTA', 'Escolta'),
        ('ALERO', 'Alero'), 
        ('ALA-PIVOT', 'Ala-Pívot'),
        ('PIVOT', 'Pívot'),
    ]
    nombre = models.CharField(max_length=100)
    posicion = models.CharField(max_length=20, choices=POSICIONES, default='BASE')  # Aquí está el campo con opciones
    numero = models.PositiveIntegerField()
    equipo = models.ForeignKey('Equipo', related_name='jugadores', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.posicion} - {self.equipo.nombre_equipo}"





# Modelo Partido
class Partido(models.Model):
    """
    Representa un partido entre dos equipos, en un campeonato.
    """
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE, null=True, blank=True)
    equipo_local = models.ForeignKey('Equipo', on_delete=models.CASCADE, related_name='partidos_local')
    equipo_visitante = models.ForeignKey('Equipo', on_delete=models.CASCADE, related_name='partidos_visitante')
    fecha = models.DateTimeField()
    estadio = models.ForeignKey('Estadio', on_delete=models.SET_NULL, null=True)
    fase = models.CharField(max_length=50, choices=[('Clasificatorias', 'Clasificatorias'), ('Cuartos', 'Cuartos'), ('Semifinal', 'Semifinal'), ('Final', 'Final')])
    goles_local = models.PositiveIntegerField(null=True, blank=True)
    goles_visitante = models.PositiveIntegerField(null=True, blank=True)
    

    def __str__(self):
        return f"{self.equipo_local.nombre_equipo} vs {self.equipo_visitante.nombre_equipo} ({self.fase})"
    
    
    
    
    
# models.py
class Cuartos(models.Model):
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE)
    equipo_local = models.ForeignKey('Equipo', on_delete=models.CASCADE, related_name='cuartos_local')
    equipo_visitante = models.ForeignKey('Equipo', on_delete=models.CASCADE, related_name='cuartos_visitante')
    fecha = models.DateTimeField()
    estadio = models.ForeignKey('Estadio', on_delete=models.SET_NULL, null=True)
    goles_local = models.PositiveIntegerField(null=True, blank=True)
    goles_visitante = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.equipo_local} vs {self.equipo_visitante} (Cuartos)"






# Modelo Estadísticas de Partido
class PartidoEstadistica(models.Model):
    """
    Representa las estadísticas de un partido entre dos equipos.
    """
    partido = models.OneToOneField(Partido, on_delete=models.CASCADE, related_name='estadisticas')
    pases_equipo_local = models.PositiveIntegerField(default=0)
    pases_equipo_visitante = models.PositiveIntegerField(default=0)
    faltas_equipo_local = models.PositiveIntegerField(default=0)
    faltas_equipo_visitante = models.PositiveIntegerField(default=0)
    triples_equipo_local = models.PositiveIntegerField(default=0)
    triples_equipo_visitante = models.PositiveIntegerField(default=0)
    rebotes_equipo_local = models.PositiveIntegerField(default=0)
    rebotes_equipo_visitante = models.PositiveIntegerField(default=0)
    puntos_equipo_local = models.PositiveIntegerField(default=0)
    puntos_equipo_visitante = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Estadísticas del partido {self.partido}"








class Posicion(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='posiciones')
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE)
    puntos = models.IntegerField(default=0)
    partidos_jugados = models.IntegerField(default=0)
    partidos_ganados = models.IntegerField(default=0)
    partidos_perdidos = models.IntegerField(default=0)

    class Meta:
        unique_together = ('equipo', 'campeonato')

    

class Campeon(models.Model):
    campeonato = models.OneToOneField('Campeonato', on_delete=models.CASCADE, related_name='campeon')
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='campeonados', null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha en que se determinó el campeón

    def __str__(self):
        return f"Campeón: {self.equipo.nombre_equipo} del Campeonato: {self.campeonato.nombre}"



class Video(models.Model):
    """
    Representa un video destacado (highlight) del campeonato.
    """
    title = models.CharField(max_length=100)  # Título del video (obligatorio)
    url = models.URLField()  # URL del video de YouTube (obligatorio)

    class Meta:
        db_table = 'basquetbol_video'  # Utilizar la tabla ya existente

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        # Puedes añadir lógica adicional aquí si deseas realizar alguna acción antes de la eliminación
        super(Video, self).delete(*args, **kwargs)