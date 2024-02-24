# Generated by Django 3.0.4 on 2024-02-24 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150, verbose_name='nombre de autor')),
                ('apellidos', models.CharField(max_length=150, verbose_name='apellidos de autor')),
                ('facebook', models.URLField(blank=True, max_length=300, null=True, verbose_name='facebook')),
                ('twitter', models.URLField(blank=True, max_length=300, null=True, verbose_name='twitter')),
                ('instagram', models.URLField(blank=True, max_length=300, null=True, verbose_name='instagram')),
                ('web', models.URLField(blank=True, max_length=300, null=True, verbose_name='web')),
                ('correo', models.EmailField(max_length=254, verbose_name='correo electronico')),
                ('estado', models.BooleanField(verbose_name='autor activo/autor no activo')),
                ('fecha_cracion', models.DateField(auto_now_add=True, verbose_name='fecha de creacion')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre de la categoria')),
                ('estado', models.BooleanField(default=True, verbose_name='categoria activada/categoria no activada')),
                ('fecha_cracion', models.DateField(auto_now_add=True, verbose_name='fecha de creacion')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
    ]
