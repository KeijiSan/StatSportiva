# Generated by Django 5.1.1 on 2024-11-21 02:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basquetbol', '0029_cuartos'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='campeon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='basquetbol.equipo'),
        ),
    ]
