from django.db import models
from django.db.models.deletion import CASCADE
from django.core.exceptions import ValidationError
from datetime import datetime
from django.utils.timezone import timezone

from usuarios.models import User


def validate_user_ssh(value):
    if len(value) > 4:
        return value
    else:
        raise ValidationError('Debe ingresar un nombre')

def validate_user_name(value):
    if len(value) > 4:
        return value
    else:
        raise ValidationError('El nombre corporativo debe contener al menos 4 caracteres')

def validate_password(value):
    if len(value) > 11:
        return value
    else:
        raise ValidationError('La contraseña debe tener un minimo de 10 caracteres')  

def validate_email(value):
    if "@test.cl" in value:
        return value
    elif "@test.com" in value:
        return value
    else:
        raise ValidationError('Email inválido, por favor ingrese email corporación')      

SUB_AREA = [
    ('Celula 1', 'Celula 1'),
    ('Celula 2', 'Celula 2'),
    ('Movil', 'Movil'),
    ('Dedicado', 'Dedicado'),
    ('Infraestructura', 'Infraestructura')
]

JOBS_AREA = [
    ('Gerente TI', 'Gerente TI'),
    ('Líder Técnico','Líder Técnico'),
    ('N1 Desarrollador Moodle', 'N1 Desarrollador Moodle'),
    ('N2 Desarrollador Moodle - Proyectos', 'N2 Desarrollador Moodle - Proyectos'),
    ('Diseñador Desarrollador','Diseñador Desarrollador'),
    ('Soporte TI', 'Soporte TI'),
    ('Servidores TI', 'Servidores TI'),
    ('Ingeniero Infraestructura', 'Ingeniero Infraestructura'),
    ('Coordinador TI', 'Coordinador TI'),
    ('Desarrollador', 'Desarrollador')
]


AREA = [
    ('TI','TI')
]
class Infraestructure(models.Model):
    #id_ssh_user     = models.AutoField(primary_key=True, null=False, default=None, verbose_name="id")
    user_ssh        = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False,verbose_name='Colaborador')
    user_email      = models.EmailField(max_length=100, default='@test.com' , verbose_name='Email', validators=[validate_email])
    user_area       = models.CharField(max_length=5, choices=AREA, null=False, default=None, verbose_name="Area") 
    sub_area        = models.CharField(max_length=100, choices=SUB_AREA, null=False, verbose_name="Sub Area")
    job_area        = models.CharField(max_length=100, choices=JOBS_AREA, null=False, verbose_name="Cargo")
    ssh_user        = models.CharField(max_length=255, validators=[validate_user_name], unique=True, verbose_name="Usuario")
    ssh_key         = models.CharField(max_length=100, validators=[validate_user_ssh], unique=True, default='', verbose_name="Nombre de llave ssh")
    ssh_password    = models.CharField(max_length=100, validators=[validate_password], unique=True, default='', verbose_name="Contraseña")
    created         = models.DateField(default=datetime.now, verbose_name="Fecha de Creación") 
    active_ssh_user = models.BooleanField(default=True, verbose_name="Usuario Activo")


    class Meta:
        verbose_name = "Listado de Cuenta"
        verbose_name_plural = "Listado de Cuentas"
        db_table = "Listado"
        ordering = ['-created']
    
    def __str__(self):
        return f'{self.sub_area} {self.ssh_user}'    