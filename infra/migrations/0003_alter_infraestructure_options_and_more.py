# Generated by Django 4.0.1 on 2022-10-04 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_alter_user_user_phone'),
        ('infra', '0002_infraestructure_user_email_infraestructure_user_ssh_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='infraestructure',
            options={'ordering': ['-created'], 'verbose_name': 'Listado de Cuenta', 'verbose_name_plural': 'Listado de Cuentas'},
        ),
        migrations.RemoveField(
            model_name='infraestructure',
            name='id_ssh_user',
        ),
        migrations.AddField(
            model_name='infraestructure',
            name='id',
            field=models.BigAutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='infraestructure',
            name='user_ssh',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.user', verbose_name='Colaborador'),
        ),
    ]