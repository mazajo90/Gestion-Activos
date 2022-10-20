# Generated by Django 4.0.1 on 2022-10-04 18:32

from django.db import migrations, models
import infra.models


class Migration(migrations.Migration):

    dependencies = [
        ('infra', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='infraestructure',
            name='user_email',
            field=models.EmailField(default='@bcnschool.cl', max_length=100, validators=[infra.models.validate_email], verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='infraestructure',
            name='user_ssh',
            field=models.CharField(default=None, max_length=100, verbose_name='Colaborador'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='infraestructure',
            name='job_area',
            field=models.CharField(choices=[('Gerente TI', 'Gerente TI'), ('Líder Técnico', 'Líder Técnico'), ('N1 Desarrollador Moodle', 'N1 Desarrollador Moodle'), ('N2 Desarrollador Moodle - Proyectos', 'N2 Desarrollador Moodle - Proyectos'), ('Diseñador Desarrollador', 'Diseñador Desarrollador'), ('Soporte TI', 'Soporte TI'), ('Servidores TI', 'Servidores TI'), ('Ingeniero Infraestructura', 'Ingeniero Infraestructura'), ('Coordinador TI', 'Coordinador TI'), ('Desarrollador', 'Desarrollador')], max_length=100, verbose_name='Cargo'),
        ),
        migrations.AlterField(
            model_name='infraestructure',
            name='ssh_key',
            field=models.CharField(default='Private_Key_AWS_', max_length=100, unique=True, validators=[infra.models.validate_user_ssh], verbose_name='Nombre de llave ssh'),
        ),
        migrations.AlterField(
            model_name='infraestructure',
            name='ssh_password',
            field=models.CharField(default='//BCN-V1.', max_length=100, unique=True, validators=[infra.models.validate_password], verbose_name='Contraseña'),
        ),
        migrations.AlterField(
            model_name='infraestructure',
            name='sub_area',
            field=models.CharField(choices=[('Celula 1', 'Celula 1'), ('Celula 2', 'Celula 2'), ('Movil', 'Movil'), ('Dedicado', 'Dedicado'), ('Infraestructura', 'Infraestructura')], max_length=100, verbose_name='Sub Area'),
        ),
    ]
