from django.db import models
from django.core.exceptions import ValidationError


def validate_id_warehouse(value):
    if value >= 1:
        return value
    else:  
        raise ValidationError('El ID debe ser mayor a 1')


class Warehouse(models.Model):
    id_warehouse = models.IntegerField(verbose_name="ID Almacer", validators=[validate_id_warehouse], primary_key=True)
    warehouse_name = models.CharField(max_length=100, verbose_name="Nombre de Almacen")

    class Meta:
        verbose_name = 'Almacen'
        verbose_name_plural = 'Almacenes'
        db_table = 'Almacen'
        ordering = ['-id_warehouse']

    def __str__(self):
        return f'{self.id_warehouse} - {self.warehouse_name}' 

