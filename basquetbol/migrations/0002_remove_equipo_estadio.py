# Generated by Django 5.1.1 on 2024-10-04 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basquetbol', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipo',
            name='estadio',
        ),
    ]
