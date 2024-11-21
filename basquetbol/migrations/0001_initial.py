# Generated by Django 5.1.1 on 2024-10-02 16:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campeonato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('descripcion', models.TextField()),
                ('max_equipos', models.PositiveIntegerField(default=10)),
                ('premios', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entrenador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('nacionalidad', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Estadio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('capacidad', models.PositiveIntegerField()),
                ('ciudad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fundacion', models.DateField()),
                ('historia', models.TextField(blank=True, null=True)),
                ('color_principal', models.CharField(help_text='Color principal en formato hexadecimal (Ej. #FF5733)', max_length=7)),
                ('color_secundario', models.CharField(help_text='Color secundario en formato hexadecimal (Ej. #33FF57)', max_length=7)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos_equipos/')),
                ('sitio_web', models.URLField(blank=True, null=True)),
                ('redes_sociales', models.JSONField(blank=True, null=True)),
                ('campeonato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipos', to='basquetbol.campeonato')),
                ('entrenador', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='basquetbol.entrenador')),
                ('estadio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='basquetbol.estadio')),
            ],
        ),
        migrations.CreateModel(
            name='Fase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('orden', models.PositiveIntegerField(help_text='Orden de la fase en el campeonato (1 para la fase inicial, etc.)')),
                ('campeonato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fases', to='basquetbol.campeonato')),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('posicion', models.CharField(max_length=50)),
                ('numero', models.PositiveIntegerField()),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jugadores', to='basquetbol.equipo')),
            ],
        ),
    ]
