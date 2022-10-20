from django.db import models
from django.db.models.deletion import CASCADE
from django.core.exceptions import ValidationError
from datetime import datetime
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

from .choices import DEPARTMENT_CHOISE, COMPANIES, USER_STATUS
from asignacion.choices import DP_BOSS


def about_upload_to(instance, filename):
    old_instance = About.objects.get(pk=instance.pk)
    old_instance.image.delete()
    return 'media/perfil' + filename  

def validate_email(value):
    if "@test.cl" in value:
        return value
    elif "@test.com" in value:
        return value
    else:
        raise ValidationError('Email inválido, por favor ingrese email corporación')

def validate_user_name_corp(value):
    if len(value) > 4:
        return value
    else:
        raise ValidationError('El nombre corporativo debe contener al menos 4 caracteres')    

def validate_user_name(value):
    if len(value) > 4:
        return value
    else:
        raise ValidationError('Ingrese un nombre')
        
def validate_user_last_name(value):
    if len(value) > 3:
        return value
    else:
        raise ValidationError('Ingrese un apellido')
    
def validate_boss(value):
    if len(value) > 2:
        return value
    else:
        raise ValidationError('Ingrese un nombre y apellido')
        

class User(models.Model):
    id_user = models.AutoField(primary_key=True, null=False, default=None, verbose_name='ID Colaborador')
    user_name = models.CharField(max_length=100, verbose_name='Nombre', validators=[validate_user_name])
    user_last_name = models.CharField(max_length=100, verbose_name='Apellido', validators=[validate_user_last_name])
    user_email = models.EmailField(max_length=100, default='@test.com' , verbose_name='Email', validators=[validate_email])
    user_phone = models.IntegerField(null=False, blank=False, unique=True, verbose_name='Numero de Telefono')
    user_name_corp = models.CharField(max_length=100, unique=True, verbose_name='Nombre corporativo', validators=[validate_user_name_corp])
    user_corp = models.CharField(max_length=100,  choices=COMPANIES, blank=False, null=False, default='Escuela de Negocios BCN School SPA',verbose_name='Empresa')
    boss_user = models.CharField(max_length=100, verbose_name='Jefe Directo', default='',blank=False, null=False, validators=[validate_boss])
    boss_user_dep = models.CharField(max_length=100, default='', choices=DEPARTMENT_CHOISE,blank=False, verbose_name='Departamento') 
    dp_boss = models.CharField(max_length=100, choices=DP_BOSS, default='' ,blank=False, verbose_name='Cargo de Jefatura')
    user_status = models.CharField( max_length=10,choices=USER_STATUS,verbose_name='Estado')
    is_activate = models.BooleanField(default=True, verbose_name='Activo')
    deparment_site = models.CharField(max_length=100, default='', verbose_name='Cargo Colaborador')
    date = models.DateField(default=timezone.now, verbose_name='Fecha de Ingreso')
    

    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'
        db_table = 'Colaborador'
        ordering = ['-user_name']

    def __str__(self):
        return f'{self.user_name} {self.user_last_name}'


    

