# basquetbol/management/commands/entrenar_modelo.py
from django.core.management.base import BaseCommand
import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from basquetbol.models import PartidoEstadistica
import random


class Command(BaseCommand):
    help = 'Entrena un modelo de predicción de partidos basado en estadísticas avanzadas'

    def handle(self, *args, **kwargs):
        self.entrenar_modelo()

    def extraer_datos(self):
        # Extraer datos de la base
        estadisticas = PartidoEstadistica.objects.select_related('partido').all()

        data = {
            'pases_equipo_local': [],
            'faltas_equipo_local': [],
            'triples_equipo_local': [],
            'rebotes_ofensivos_local': [],
            'rebotes_defensivos_local': [],
            'robos_equipo_local': [],
            'puntos_equipo_local': [],
            'pases_equipo_visitante': [],
            'faltas_equipo_visitante': [],
            'triples_equipo_visitante': [],
            'rebotes_ofensivos_visitante': [],
            'rebotes_defensivos_visitante': [],
            'robos_equipo_visitante': [],
            'puntos_equipo_visitante': [],
            'resultado': [],
        }

        # Cargar datos existentes
        for estadistica in estadisticas:
            data['pases_equipo_local'].append(estadistica.pases_equipo_local)
            data['faltas_equipo_local'].append(estadistica.faltas_equipo_local)
            data['triples_equipo_local'].append(estadistica.triples_equipo_local)
            data['rebotes_ofensivos_local'].append(estadistica.rebotes_ofensivos_equipo_local)
            data['rebotes_defensivos_local'].append(estadistica.rebotes_defensivos_equipo_local)
            data['robos_equipo_local'].append(estadistica.robos_equipo_local)
            data['puntos_equipo_local'].append(estadistica.puntos_equipo_local)
            data['pases_equipo_visitante'].append(estadistica.pases_equipo_visitante)
            data['faltas_equipo_visitante'].append(estadistica.faltas_equipo_visitante)
            data['triples_equipo_visitante'].append(estadistica.triples_equipo_visitante)
            data['rebotes_ofensivos_visitante'].append(estadistica.rebotes_ofensivos_equipo_visitante)
            data['rebotes_defensivos_visitante'].append(estadistica.rebotes_defensivos_equipo_visitante)
            data['robos_equipo_visitante'].append(estadistica.robos_equipo_visitante)
            data['puntos_equipo_visitante'].append(estadistica.puntos_equipo_visitante)

            if estadistica.puntos_equipo_local > estadistica.puntos_equipo_visitante:
                data['resultado'].append(1)  # Local ganó
            else:
                data['resultado'].append(0)  # Visitante ganó

        # Generar datos adicionales (ficticios) para reforzar el modelo
        for _ in range(200):  # Generar 200 filas adicionales
            data['pases_equipo_local'].append(random.randint(10, 50))
            data['faltas_equipo_local'].append(random.randint(5, 20))
            data['triples_equipo_local'].append(random.randint(0, 10))
            data['rebotes_ofensivos_local'].append(random.randint(5, 15))
            data['rebotes_defensivos_local'].append(random.randint(10, 25))
            data['robos_equipo_local'].append(random.randint(0, 10))
            puntos_local = random.randint(50, 120)
            data['puntos_equipo_local'].append(puntos_local)

            data['pases_equipo_visitante'].append(random.randint(10, 50))
            data['faltas_equipo_visitante'].append(random.randint(5, 20))
            data['triples_equipo_visitante'].append(random.randint(0, 10))
            data['rebotes_ofensivos_visitante'].append(random.randint(5, 15))
            data['rebotes_defensivos_visitante'].append(random.randint(10, 25))
            data['robos_equipo_visitante'].append(random.randint(0, 10))
            puntos_visitante = random.randint(50, 120)
            data['puntos_equipo_visitante'].append(puntos_visitante)

            if puntos_local > puntos_visitante:
                data['resultado'].append(1)  # Local ganó
            else:
                data['resultado'].append(0)  # Visitante ganó

        df = pd.DataFrame(data)
        return df

    def entrenar_modelo(self):
        # Extraer los datos
        df = self.extraer_datos()

        # Verificar si los datos están completos
        if df.empty:
            self.stdout.write(self.style.ERROR('No hay suficientes datos para entrenar el modelo.'))
            return

        # Definir las características y la variable objetivo
        X = df.drop(columns=['resultado'])
        y = df['resultado']

        # Dividir los datos en entrenamiento y prueba
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Crear y entrenar el modelo
        model = RandomForestClassifier(n_estimators=150, random_state=42, max_depth=10)
        model.fit(X_train, y_train)

        # Guardar el modelo en una ubicación fija
        model_path = os.path.join('media', 'modelos', 'modelo_prediccion_partidos_avanzado.pkl')
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        joblib.dump(model, model_path)

        # Evaluar el modelo
        train_accuracy = model.score(X_train, y_train)
        test_accuracy = model.score(X_test, y_test)

        # Imprimir resultados
        self.stdout.write(self.style.SUCCESS(f'Modelo entrenado exitosamente.'))
        self.stdout.write(self.style.SUCCESS(f'Precisión en entrenamiento: {train_accuracy:.2f}'))
        self.stdout.write(self.style.SUCCESS(f'Precisión en prueba: {test_accuracy:.2f}'))
