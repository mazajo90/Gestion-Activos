from django.db import models
from django.db.models.deletion import CASCADE
from datetime import datetime
from django.core.exceptions import ValidationError
import random
import string


from catastro_equipos.models import Product, ProductStatus 
from usuarios.models import User
from .choices import DP_BOSS, ASIGN_STATUS


from ckeditor.fields import RichTextField


def random_id(lenght=6):
    return ''.join(random.choice(string.digits) for x in range(lenght))

def validate_boss(value):
    if len(value) > 2:
        return value
    else:
        raise ValidationError('Ingrese un nombre y apellido')     

class AsignationState(models.Model):
    id_asig_status = models.AutoField( primary_key=True, null=False, default=None, verbose_name='ID Estado Asignación')
    asignation_status = models.CharField(max_length=10, choices=ASIGN_STATUS, verbose_name='Estado de Asignacion')
    
    
    class Meta:
        verbose_name = 'Estado de Asignacion'
        verbose_name_plural = 'Estado de Asignaciones'
        db_table = 'EstadoAsignacion'
        ordering = ['id_asig_status']

    def __str__(self):
        return f'{self.id_asig_status} - {self.asignation_status}'
        

class Asignation(models.Model):
    asig_id = models.IntegerField(null=False, blank=False, default=random_id, unique=True, verbose_name='ID de Asignación', primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Colaborador')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Producto Asignado', null=False, blank=False)
    product_status = models.ForeignKey(ProductStatus, on_delete=models.CASCADE, verbose_name='Estado de Producto')
    id_asig_status = models.ForeignKey(AsignationState, on_delete=models.CASCADE, verbose_name='ID Estado Asignación')
    date = models.DateField(default=datetime.now, blank=True, null=True, verbose_name='Fecha de Asignación')
    dp_boss = models.CharField(max_length=100, choices=DP_BOSS, default='Seleccione un Departamento' ,blank=False, verbose_name='Departamento a Cargo')
    boss = models.CharField(max_length=100, verbose_name='Autorizado por (Jefe)', blank=False, null=False, validators=[validate_boss])
    acta_ent = RichTextField(blank=False, null=False, verbose_name='Acta de entrega')
    

    class Meta:
        verbose_name = ("Equipo Asignado")
        verbose_name_plural = ("Equipos Asignados")
        db_table = "EquiposAsignados"
        ordering = ['-date', 'product', 'user']

    def __str__(self):
        return f'{self.asig_id} {self.product} - {self.user}'
    

class AsignationHistory(models.Model):
    asig_id        = models.IntegerField(null=False, blank=False, verbose_name='ID de Asignacion')
    product        = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, verbose_name='Producto Asignado')
    product_status = models.ForeignKey(ProductStatus, on_delete=models.SET_NULL, null=True, verbose_name='Estado de Producto')
    user           = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Colaborador')
    date_init      = models.DateField(default=datetime.now, blank=False, null=False, verbose_name='Fecha de Entrega')
    date_fin       = models.DateField(default=datetime.now, blank=False, null=False, verbose_name='Fecha de Retiro')
    observation    = RichTextField(blank=False, null=False, verbose_name='Observación')
        
    class Meta:
        verbose_name = ('Historial')
        verbose_name_plural = ('Historiales')
        db_table = 'Historial'
        ordering = ['-asig_id']
     
    def __str__(self):
        return f'{self.asig_id} {self.product} {self.user}'    