# Generated by Django 4.2.6 on 2023-10-28 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trafico', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trafico',
            name='cliente',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Cliente'),
        ),
        migrations.AddField(
            model_name='trafico',
            name='comentario',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Comentario'),
        ),
        migrations.AddField(
            model_name='trafico',
            name='pais',
            field=models.CharField(blank=True, choices=[('GUATEMALA', 'GUATEMALA'), ('EL SALVADOR', 'EL SALVADOR'), ('HONDURAS', 'HONDURAS'), ('NICARAGUA', 'NICARAGUA'), ('COSTA RICA', 'COSTA RICA'), ('PANAMA', 'PANAMA')], default=None, max_length=50, null=True, verbose_name='País'),
        ),
        migrations.AddField(
            model_name='trafico',
            name='restaurante',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Restaurante'),
        ),
        migrations.AddField(
            model_name='trafico',
            name='telefono',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Télefono'),
        ),
        migrations.AddField(
            model_name='trafico',
            name='usuario',
            field=models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Encargado'),
        ),
    ]