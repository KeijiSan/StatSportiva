# basquetbol/management/commands/entrenar_modelo.py
from django.core.management.base import BaseCommand
import sys
import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from basquetbol.models import PartidoEstadistica

class Command(BaseCommand):
    help = 'Entrena un modelo de predicción de partidos'

    def handle(self, *args, **kwargs):
        self.entrenar_modelo()

    def extraer_datos(self):
        estadisticas = PartidoEstadistica.objects.all()

        data = {
            'pases_equipo_local': [],
            'faltas_equipo_local': [],
            'triples_equipo_local': [],
            'rebotes_equipo_local': [],
            'puntos_equipo_local': [],
            'pases_equipo_visitante': [],
            'faltas_equipo_visitante': [],
            'triples_equipo_visitante': [],
            'rebotes_equipo_visitante': [],
            'puntos_equipo_visitante': [],
            'resultado': [],
        }

        for estadistica in estadisticas:
            data['pases_equipo_local'].append(estadistica.pases_equipo_local)
            data['faltas_equipo_local'].append(estadistica.faltas_equipo_local)
            data['triples_equipo_local'].append(estadistica.triples_equipo_local)
            data['rebotes_equipo_local'].append(estadistica.rebotes_equipo_local)
            data['puntos_equipo_local'].append(estadistica.puntos_equipo_local)
            data['pases_equipo_visitante'].append(estadistica.pases_equipo_visitante)
            data['faltas_equipo_visitante'].append(estadistica.faltas_equipo_visitante)
            data['triples_equipo_visitante'].append(estadistica.triples_equipo_visitante)
            data['rebotes_equipo_visitante'].append(estadistica.rebotes_equipo_visitante)
            data['puntos_equipo_visitante'].append(estadistica.puntos_equipo_visitante)

            if estadistica.puntos_equipo_local > estadistica.puntos_equipo_visitante:
                data['resultado'].append(1)
            else:
                data['resultado'].append(0)

        df = pd.DataFrame(data)
        return df

    def entrenar_modelo(self):
        # Extraer los datos
        df = self.extraer_datos()

        # Definir las características y la variable objetivo
        X = df.drop(columns=['resultado'])
        y = df['resultado']

        # Dividir los datos en entrenamiento y prueba
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Crear y entrenar el modelo
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Guardar el modelo
        joblib.dump(model, 'modelo_prediccion_partidos.pkl')

        # Imprimir la precisión
        accuracy = model.score(X_test, y_test)
        self.stdout.write(self.style.SUCCESS(f'Accuracy: {accuracy:.2f}'))
