# Generated by Django 4.2.6 on 2023-10-09 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServicioCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(blank=True, max_length=100, null=True, verbose_name='Télefono')),
                ('checkin', models.CharField(blank=True, max_length=50, null=True, verbose_name='Agregado')),
                ('restaurante', models.CharField(blank=True, max_length=50, null=True, verbose_name='Restaurante')),
                ('cliente', models.CharField(blank=True, max_length=100, null=True, verbose_name='Colonia')),
                ('pais', models.CharField(blank=True, choices=[('GUATEMALA', 'GUATEMALA'), ('EL SALVADOR', 'EL SALVADOR'), ('HONDURAS', 'HONDURAS'), ('NICARAGUA', 'NICARAGUA'), ('COSTA RICA', 'COSTA RICA'), ('PANAMA', 'PANAMA')], default=None, max_length=50, null=True, verbose_name='País')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='actualizacion')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creación')),
            ],
            options={
                'verbose_name': 'Servicio al Cliente',
                'verbose_name_plural': 'Servicio Clientes',
                'db_table': 'ServicioCliente',
                'ordering': ['-created_at'],
                'default_related_name': 'ServicioCliente',
            },
        ),
    ]