# Generated by Django 4.0.1 on 2022-10-04 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infra', '0003_alter_infraestructure_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='infraestructure',
            name='user_area',
            field=models.CharField(choices=[('TI', 'TI')], default=None, max_length=5, verbose_name='Area'),
        ),
    ]
