# Generated by Django 5.1.1 on 2024-11-16 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basquetbol', '0006_partido_campeonato'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partido',
            name='campeonato',
        ),
    ]