# Generated by Django 4.0.4 on 2022-05-26 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0028_alter_elemento_foto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipos_Elemento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(choices=[('Accesorios', 'Accesorios'), ('Productos', 'Productos')], max_length=20, verbose_name='Categoría')),
                ('subcategoria', models.CharField(max_length=20, unique=True, verbose_name='Subcategoría')),
            ],
        ),
        migrations.AlterField(
            model_name='elemento',
            name='tipo_elemento',
            field=models.ForeignKey(null='False', on_delete=django.db.models.deletion.SET_NULL, to='administrador.tipos_elemento', verbose_name='Categoria'),
        ),
    ]