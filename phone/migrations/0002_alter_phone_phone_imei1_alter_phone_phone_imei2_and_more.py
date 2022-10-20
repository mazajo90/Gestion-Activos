# Generated by Django 4.0.1 on 2022-09-30 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='phone_imei1',
            field=models.IntegerField(unique=True, verbose_name='IMEI 1'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='phone_imei2',
            field=models.IntegerField(unique=True, verbose_name='IMEI 2'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='phone_name',
            field=models.CharField(choices=[('NOKIA', 'NOKIA'), ('SAMSUNG', 'SAMSUNG'), ('MOTOROLA', 'MOTOROLA')], max_length=100, verbose_name='Marca de Producto'),
        ),
    ]