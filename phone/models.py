from django.db import models
from django.db.models.deletion import CASCADE
from datetime import datetime
from django.core.exceptions import ValidationError

from catastro_equipos.choices import PHONE_CHOICES, PHONE_TYPE, PRODUCT_STATUS
from catastro_equipos.models import ProductStatus


def validate_product_data(value):
    if len(value) > 1:
        return value
    else:
        raise ValidationError('Por favor, Ingrese descripcion valida')
    
    
def validate_product_quantity(value):
    if value >= 1:
        return value
    else:  
        raise ValidationError('La cantidad debe ser mayor o igual a 1')

class Phone(models.Model):
    phone_id       = models.AutoField(primary_key=True, null=False, default=None, verbose_name='ID Estado de Producto')
    phone_type     = models.CharField(max_length=20, default='', choices=PHONE_CHOICES, verbose_name='Tipo de Producto')
    phone_name     = models.CharField(max_length=100, blank=False, null=False, choices=PHONE_TYPE, verbose_name='Marca de Producto')
    phone_model    = models.CharField(max_length=100, verbose_name='Modelo de Producto', validators=[validate_product_data])
    phone_imei1    = models.IntegerField(unique=True,verbose_name='IMEI 1')
    phone_imei2    = models.IntegerField(unique=True,verbose_name='IMEI 2')
    phone_serial   = models.CharField(max_length=100, unique=True, blank=False, null=False, verbose_name='Serial', default=0)
    phone_status   = models.CharField(max_length=10, choices=PRODUCT_STATUS, default='Nuevo', blank=False, null=False, verbose_name='Estado')
    phone_created  = models.DateField(default=datetime.now, verbose_name='Fecha de creacion')
    phone_number   = models.IntegerField(verbose_name='Numero de Teléfono')
    phone_quantity = models.IntegerField(verbose_name='Cantidad', default= 1, validators=[validate_product_quantity])
    phone_buy      = models.DateField(default=datetime.now, verbose_name='Fecha de compra')
    
    class Meta:
        verbose_name = 'Celular'
        verbose_name_plural = 'Celulares'
        db_table = 'Celular'
        ordering = ['-phone_created']

    def __str__(self):
        return f'{self.phone_name} - {self.phone_serial}'
