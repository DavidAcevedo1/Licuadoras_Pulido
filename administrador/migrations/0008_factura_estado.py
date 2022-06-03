# Generated by Django 4.0.3 on 2022-05-18 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0007_elemento_marca'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='estado',
            field=models.CharField(choices=[('Pagado', 'Pagado'), ('Anulado', 'Anulado')], default='Pagado', max_length=20, verbose_name='Estado'),
        ),
    ]