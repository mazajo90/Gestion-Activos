# Generated by Django 3.0.6 on 2022-05-18 20:48

import accesorios.models
import ckeditor.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catastro_equipos', '__first__'),
        ('usuarios', '__first__'),
        ('warehouse', '__first__'),
        ('asignacion', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisplayPC',
            fields=[
                ('id_product', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('display_name', models.CharField(max_length=100, validators=[accesorios.models.validate_display_name], verbose_name='Marca de Monitor')),
                ('display_model', models.CharField(max_length=100, verbose_name='Modelo')),
                ('display_size', models.CharField(choices=[('24"', '24"'), ('27"', '27"'), ('32"', '32"'), ('40"', '40"'), ('64"', '64"')], default='Seleccione', max_length=5, verbose_name='Pulgadas')),
                ('display_tech', models.CharField(choices=[('LED', 'LED'), ('LCD', 'LCD')], default='Seleccione', max_length=10, verbose_name='Tipo de Monitor')),
                ('active_code', models.CharField(default='BCN', max_length=20, unique=True, verbose_name='Codigo Activo')),
                ('serial', models.CharField(default=0, max_length=100, unique=True, verbose_name='Serial')),
                ('display_quantity', models.IntegerField(default=1, validators=[accesorios.models.validate_display_quantity], verbose_name='Cantidad')),
                ('asig_id', models.IntegerField(default=accesorios.models.random_id, unique=True, verbose_name='ID de Asignacion')),
                ('created', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de compra')),
                ('product_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catastro_equipos.ProductStatus', verbose_name='Estado')),
                ('warehouse', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='warehouse.Warehouse', verbose_name='Bodega')),
            ],
            options={
                'verbose_name': 'Monitor',
                'verbose_name_plural': 'Monitores',
                'db_table': 'Monitor',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='AsignationDisplayHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asig_id', models.IntegerField(verbose_name='ID de Asignacion')),
                ('date_init', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de Entrega')),
                ('date_fin', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de Retiro')),
                ('observation', ckeditor.fields.RichTextField(verbose_name='Observaci??n')),
                ('display_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accesorios.DisplayPC', verbose_name='Monitor Asignado')),
                ('product_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catastro_equipos.ProductStatus', verbose_name='Estado de Producto')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.User', verbose_name='Colaborador')),
            ],
            options={
                'verbose_name': 'Historial Pantalla',
                'verbose_name_plural': 'Historiales de Pantallas',
                'db_table': 'Historial_Pantalla',
                'ordering': ['-asig_id'],
            },
        ),
        migrations.CreateModel(
            name='AsignationDisplay',
            fields=[
                ('asig_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de Asignaci??n')),
                ('date', models.DateField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Fecha de Asignaci??n')),
                ('dep_boss', models.CharField(choices=[('Directora de Proyecto', 'Directora de Proyecto'), ('Jefe de Auditoria y Control Interno', 'Jefe de Auditoria y Control Interno'), ('Coordinador Acad??mico', 'Coordinador Acad??mico'), ('Director(a) de Proyecto', 'Director(a) de Proyecto'), ('Jefe de Coordinaci??n Acad??mica', 'Jefe de Coordinaci??n Acad??mica'), ('Key Account Manager', 'Key Account Manager'), ('Encargado de Log??stica y Control de Stock', 'Encargado de Log??stica y Control de Stock'), ('Lider T??cnico', 'Lider T??cnico'), ('Dise??ador Multimedia y Jefe T??cnico', 'Dise??ador Multimedia y Jefe T??cnico'), ('Office Manager - Comunicaciones Internas y Jefa de coordinaci??n acad??mica', 'Office Manager - Comunicaciones Internas y Jefa de coordinaci??n acad??mica'), ('Gerente General', 'Gerente General'), ('Jefe de Capacitaci??n y Desarrollo Organizacional', 'Jefe de Capacitaci??n y Desarrollo Organizacional'), ('Directora de Proyecto Junior', 'Directora de Proyecto Junior'), ('Gerente de Capacitaci??n', 'Gerente de Capacitaci??n'), ('Gerente Comercial', 'Gerente Comercial'), ('Subgerenta de Proyectos', 'Subgerenta de Proyectos'), ('Gerente de Marketing y Comunicaciones', 'Gerente de Marketing y Comunicaciones'), ('Subgerente TI', 'Subgerente TI')], max_length=100, verbose_name='Departamento a Cargo')),
                ('boss', models.CharField(max_length=100, validators=[accesorios.models.validate_boss], verbose_name='Autorizado por (Jefe)')),
                ('acta_ent', ckeditor.fields.RichTextField(verbose_name='Acta de entrega')),
                ('asignation_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asignacion.AsignationState', verbose_name='Estado de Asignaci??n')),
                ('display_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accesorios.DisplayPC', verbose_name='Producto Asignado')),
                ('product_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catastro_equipos.ProductStatus', verbose_name='Estado de Producto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.User', verbose_name='Colaborador')),
            ],
            options={
                'verbose_name': 'Monitor Asignado',
                'verbose_name_plural': 'Monitores Asignados',
                'db_table': 'MonitorAsignacion',
                'ordering': ['-date', 'display_name', 'user'],
            },
        ),
    ]
