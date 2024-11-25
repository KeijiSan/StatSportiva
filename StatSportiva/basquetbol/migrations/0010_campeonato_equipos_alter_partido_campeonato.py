# Generated by Django 5.1.1 on 2024-11-16 18:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basquetbol', '0009_alter_equipo_campeonato_alter_equipo_color_principal_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='campeonato',
            name='equipos',
            field=models.ManyToManyField(related_name='campeonatos', to='basquetbol.equipo'),
        ),
        migrations.AlterField(
            model_name='partido',
            name='campeonato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partidos', to='basquetbol.campeonato'),
        ),
    ]