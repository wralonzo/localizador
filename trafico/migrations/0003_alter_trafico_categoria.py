# Generated by Django 4.2.6 on 2023-10-28 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categoriatrafico', '__first__'),
        ('trafico', '0002_trafico_cliente_trafico_comentario_trafico_pais_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trafico',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='categoriatrafico.categoriatrafico', verbose_name='Categoria'),
        ),
    ]
