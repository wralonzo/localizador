# Generated by Django 4.2.6 on 2023-10-28 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'default_related_name': 'Categoría servicio al cliente', 'ordering': ['-created_at'], 'verbose_name': 'Categoría servicio al cliente', 'verbose_name_plural': 'Categoría servicio al cliente'},
        ),
    ]