from django.db import models
from django.db.models.deletion import CASCADE
from datetime import datetime
from django.core.exceptions import ValidationError

from .choices import TYPE_NOTEBOOK_MODEL, TYPE_PRODUCT, HARD_DISK, HARD_DISK_MODEL, RAM_CHOICES, RAM_TYPE, DEPARTMENT_CHOISE, PROCESSOR_UNID, USER_STATUS, PRODUCT_STATUS, HARD_DISK_TYPE, SERIAL_CHOICES   

from usuarios.models import User
from warehouse.models import Warehouse


def about_upload_to(instance, filename):
    old_instance = About.objects.get(pk=instance.pk)
    old_instance.image.delete()
    return 'media/' + filename

def validate_product_quantity(value):
    if value >= 1:
        return value
    else:  
        raise ValidationError('La cantidad debe ser mayor o igual a 1')

def validate_product_data(value):
    if len(value) > 1:
        return value
    else:
        raise ValidationError('Por favor, Ingrese descripcion valida')           


class ProductStatus(models.Model):
    id_product_status = models.AutoField(primary_key=True, null=False, default=None, verbose_name='ID Estado de Producto')
    product_status = models.CharField(max_length=10, choices=PRODUCT_STATUS, default='Nuevo', blank=False, null=False, verbose_name='Estado del Equipo')
    
    class Meta:
        verbose_name = 'Estado de Producto'
        verbose_name_plural = 'Estado de Productos'
        db_table = 'Estado_Producto'
        ordering = ['id_product_status']

    def __str__(self):
        return f'{self.id_product_status} - {self.product_status}'



class Product(models.Model):
    id_product = models.AutoField(primary_key=True, null=False, default=None, verbose_name='ID Producto')
    product_name = models.CharField(max_length=100, blank=False, null=False, choices=TYPE_NOTEBOOK_MODEL,verbose_name='Marca producto', validators=[validate_product_data])
    type_product = models.CharField(choices=TYPE_PRODUCT, max_length=20, default='', verbose_name='Producto')
    model_product = models.CharField(max_length=100, verbose_name='Modelo')
    mac_address = models.CharField(max_length=50, unique=True, blank=True, null=True, verbose_name='Direccion Mac')
    type_serial = models.CharField(max_length=10, choices=SERIAL_CHOICES, blank=True, null=True, verbose_name='Tipo de Serial')
    ram_pc = models.CharField(max_length=5, verbose_name='Ram instalada', blank=True, choices=RAM_CHOICES,default='8')
    ram_pc_type = models.CharField(max_length=5, verbose_name='Tipo de Ram', blank=True, choices=RAM_TYPE,default='DD4')
    disk_pc = models.CharField(max_length=50, default='128 GB', blank=True, choices=HARD_DISK_TYPE,verbose_name='Capacidad de Disco Duro')
    disk_pc_type = models.CharField(max_length=10, default='SDD', blank=True, verbose_name='Tipo de Disco', choices=HARD_DISK)
    disk_pc_model = models.CharField(max_length=10, default='NVME', blank=True, verbose_name='Modelo de Disco', choices=HARD_DISK_MODEL)
    processor = models.CharField(max_length=5, choices=PROCESSOR_UNID, blank=True, null=True, default='----', verbose_name='Procesador')
    processor_model = models.CharField(max_length=100, blank=True, null=True, verbose_name='Modelo de Procesador')
    serial = models.CharField(max_length=100, unique=True, blank=False, null=False, verbose_name='Serial', default=0)
    active_code = models.CharField(max_length=20, default='BCN', verbose_name='Codigo Activo', unique=True)
    created = models.DateField(default=datetime.now, verbose_name='Fecha de creacion')
    product_quantity = models.IntegerField(verbose_name='Cantidad', default= 1, validators=[validate_product_quantity])
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, verbose_name='Almacen', null=True)
    product_status = models.ForeignKey(ProductStatus, on_delete=models.CASCADE, verbose_name='Estado de Producto')
    buy_product = models.DateField(default=datetime.now, verbose_name='Fecha de compra')
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'Producto'
        ordering = ['-created']

    def __str__(self):
        return f'{self.product_name} - {self.serial}'  



 

