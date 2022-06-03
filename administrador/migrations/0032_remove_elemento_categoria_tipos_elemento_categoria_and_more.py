# Generated by Django 4.0.4 on 2022-05-26 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0031_remove_tipos_elemento_categoria_elemento_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elemento',
            name='categoria',
        ),
        migrations.AddField(
            model_name='tipos_elemento',
            name='categoria',
            field=models.CharField(choices=[('Accesorios', 'Accesorios'), ('Productos', 'Productos')], default='Accesorios', max_length=20, verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='elemento',
            name='tipo_elemento',
            field=models.ForeignKey(null='False', on_delete=django.db.models.deletion.SET_NULL, to='administrador.tipos_elemento', verbose_name='Subcategoría'),
        ),
    ]