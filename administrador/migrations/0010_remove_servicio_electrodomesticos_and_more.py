# Generated by Django 4.0.3 on 2022-05-20 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0009_rename_electrodomesticos_electrodomestico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicio',
            name='electrodomesticos',
        ),
        migrations.AddField(
            model_name='servicio',
            name='electrodomestico',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administrador.electrodomestico', verbose_name='Electrodomestico'),
        ),
    ]