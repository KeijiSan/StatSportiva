# apps.py

from django.apps import AppConfig

class BasquetbolConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'basquetbol'

    def ready(self):
        # Este mensaje es útil para saber que los signals se han cargado correctamente
        print("Aplicación de Basquetbol lista, cargando signals...")
        
        # Importamos los signals aquí para que se registren al iniciar la aplicación
        import basquetbol.signals
