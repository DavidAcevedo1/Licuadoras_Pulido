# Generated by Django 4.0.3 on 2022-09-25 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('Rid', models.AutoField(primary_key=True, serialize=False)),
                ('Rnombre', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'usuarios_rol',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('Uid', models.AutoField(primary_key=True, serialize=False)),
                ('documento', models.CharField(max_length=10, unique=True)),
                ('tipo_documento', models.CharField(choices=[('C.C', 'C.C'), ('T.I', 'T.I'), ('C.E', 'C.E')], max_length=3, verbose_name='Tipo documento')),
                ('rol', models.CharField(blank=True, choices=[('Administrador', 'Administrador'), ('Proveedor', 'Proveedor'), ('Cliente', 'Cliente')], max_length=13, verbose_name='rol')),
                ('Unombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('celular', models.CharField(max_length=10, unique=True)),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo'), ('Anulado', 'Anulado')], default='Activo', max_length=10, verbose_name='Estado')),
            ],
            options={
                'db_table': 'usuarios_usuario',
            },
        ),
    ]
