from django.apps import AppConfig


class BasquetbolConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'basquetbol'

# apps.py
from django.apps import AppConfig

class BasquetbolConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'basquetbol'

    def ready(self):
        import basquetbol.signals
from django.apps import AppConfig

class BasquetbolConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'basquetbol'

    def ready(self):
        import basquetbol.signals  # Asegúrate de importar los signals aquí


class BasquetbolConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'basquetbol'

    def ready(self):
        print("Aplicación de Basquetbol lista, cargando signals...")
        import basquetbol.signals
