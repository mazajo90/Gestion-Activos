from django.db import models
from django.db.models.deletion import CASCADE
from datetime import datetime
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField
import random
import string


from catastro_equipos.models import Product, ProductStatus
from asignacion.models import Asignation, AsignationState
from warehouse.models import Warehouse
from usuarios.models import User 
from .choices import TYPE_DISPLAY, INCH
from asignacion.choices import DP_BOSS

def random_id(lenght=4):
    return ''.join(random.choice(string.digits) for x in range(lenght))


def validate_display_quantity(value):
    if value >= 1:
        return value
    else:  
        raise ValidationError('La cantidad debe ser mayor o igual a 1')

def validate_display_name(value):
    if len(value) > 1:
        return value
    else:
        raise ValidationError('Por favor, Ingrese descripcion valida')

def validate_boss(value):
    if len(value) > 2:
        return value
    else:
        raise ValidationError('Ingrese un nombre y apellido')

class DisplayPC(models.Model):
    id_product       = models.AutoField(primary_key=True, unique=True, verbose_name='ID')
    display_name     = models.CharField(max_length=100, blank=False, null=False, verbose_name='Marca de Monitor', validators=[validate_display_name])
    display_model    = models.CharField(max_length=100, blank=False, null=False, verbose_name='Modelo')
    display_size     = models.CharField(max_length=5, choices=INCH, blank=False, null=False, verbose_name='Pulgadas', default='Seleccione')
    display_tech     = models.CharField(max_length=10, choices=TYPE_DISPLAY, blank=False, null=False, verbose_name='Tipo de Monitor',default='Seleccione')
    active_code      = models.CharField(max_length=20, default='BCN', unique=True, verbose_name='Codigo Activo')
    serial           = models.CharField(max_length=100, unique=True, blank=False, null=False, verbose_name='Serial', default=0)
    display_quantity = models.IntegerField(default=1, null=False, verbose_name='Cantidad', validators=[validate_display_quantity])
    warehouse        = models.ForeignKey(Warehouse, on_delete=models.SET_NULL, null=True, verbose_name='Bodega')   
    product_status   = models.ForeignKey(ProductStatus, on_delete=models.SET_NULL, null=True, verbose_name='Estado')
    asig_id          = models.IntegerField(unique=True, default=random_id, null=False, verbose_name='ID de Asignacion')    
    created          = models.DateField(default=datetime.now, verbose_name='Fecha de compra')
    
    class Meta:
        verbose_name = 'Monitor'
        verbose_name_plural = 'Monitores'
        db_table = 'Monitor'
        ordering = ['-created']

    def __str__(self):
        return f'{self.asig_id} {self.display_name} {self.active_code}'  

class AsignationDisplay(models.Model):
    asig_id = models.AutoField(primary_key=True, null=False, blank=False, verbose_name='ID de Asignación')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Colaborador')
    display_name = models.ForeignKey(DisplayPC, on_delete=models.CASCADE, verbose_name='Producto Asignado', null=False, blank=False)
    product_status = models.ForeignKey(ProductStatus, on_delete=models.CASCADE, verbose_name='Estado de Producto')
    asignation_status = models.ForeignKey(AsignationState, on_delete=models.CASCADE, verbose_name='Estado de Asignación')
    date = models.DateField(default=datetime.now, blank=True, null=True, verbose_name='Fecha de Asignación')
    dep_boss = models.CharField(max_length=100, choices=DP_BOSS ,blank=False, verbose_name='Departamento a Cargo')
    boss = models.CharField(max_length=100, verbose_name='Autorizado por (Jefe)', blank=False, null=False, validators=[validate_boss])
    acta_ent = RichTextField(blank=False, null=False, verbose_name='Acta de entrega')
    

    class Meta:
        verbose_name = ("Monitor Asignado")
        verbose_name_plural = ("Monitores Asignados")
        db_table = "MonitorAsignacion"
        ordering = ['-date', 'display_name', 'user']

    def __str__(self):
        return f'{self.asig_id} {self.display_name} - {self.user}'   
    

class AsignationDisplayHistory(models.Model):
    asig_id        = models.IntegerField(null=False, blank=False, verbose_name='ID de Asignacion')
    display_name   = models.ForeignKey(DisplayPC, on_delete=models.SET_NULL, null=True, verbose_name='Monitor Asignado')
    product_status = models.ForeignKey(ProductStatus, on_delete=models.SET_NULL, null=True, verbose_name='Estado de Producto')
    user           = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Colaborador')
    date_init      = models.DateField(default=datetime.now, blank=False, null=False, verbose_name='Fecha de Entrega')
    date_fin       = models.DateField(default=datetime.now, blank=False, null=False, verbose_name='Fecha de Retiro')
    observation    = RichTextField(blank=False, null=False, verbose_name='Observación')
        
    class Meta:
        verbose_name = 'Historial Pantalla'
        verbose_name_plural = 'Historiales de Pantallas'
        db_table = 'Historial_Pantalla'
        ordering = ['-asig_id']
     
    def __str__(self):
        return f'{self.asig_id} {self.display_name} {self.user}'        