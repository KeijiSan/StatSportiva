# Generated by Django 5.1.1 on 2024-11-16 20:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basquetbol', '0014_alter_campeonato_nombre_alter_partido_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partido',
            name='campeonato',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basquetbol.campeonato'),
        ),
    ]
