# Generated by Django 3.0.3 on 2020-03-05 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=250)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('name', models.CharField(max_length=80)),
                ('surname', models.CharField(max_length=80)),
            ],
        ),
    ]