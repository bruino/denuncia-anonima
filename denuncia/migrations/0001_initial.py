# Generated by Django 2.2.3 on 2019-07-26 13:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Denuncia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('nombre_apellido_sospechoso', models.CharField(blank=True, max_length=100)),
                ('apodo_sospechoso', models.CharField(blank=True, max_length=100)),
                ('descripcion', models.TextField(blank=True, max_length=300)),
                ('locacion', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]