# Generated by Django 3.0.3 on 2020-03-20 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alojamientos', '0002_auto_20200320_0158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alojamiento',
            old_name='autor',
            new_name='autor_id',
        ),
        migrations.RenameField(
            model_name='comentario',
            old_name='alojamiento',
            new_name='alojamiento_id',
        ),
        migrations.RenameField(
            model_name='comentario',
            old_name='autor',
            new_name='autor_id',
        ),
    ]
