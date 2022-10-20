from django.conf import settings
from django.contrib.admin.widgets import AdminDateWidget 
from django import forms 
from django.core.mail import send_mail, EmailMessage

from .models import Product, ProductStatus
from .choices import TYPE_PRODUCT, PRODUCT_STATUS, PROCESSOR_UNID, HARD_DISK_TYPE, HARD_DISK, HARD_DISK_MODEL, RAM_CHOICES, RAM_TYPE, SERIAL_CHOICES, TYPE_NOTEBOOK_MODEL

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'id_product',
            'product_name',
            'type_product',
            'model_product',
            'mac_address',
            'type_serial',
            'ram_pc',
            'ram_pc_type',
            'disk_pc',
            'disk_pc_type',
            'disk_pc_model',
            'processor',
            'processor_model',
            'serial',
            'active_code',
            'product_quantity',
            'warehouse',
            'product_status',
            'buy_product'
        ]
        widgets= {
            'id_product': forms.TextInput(
              attrs = {
                  'class':'form-control',
                  'readonly' : True
              }  
            ),
            'product_name': forms.Select(
                choices=TYPE_NOTEBOOK_MODEL,
                attrs = {
                    'class':'form-control'
                    
                }
            ),
            'type_product': forms.Select(
                choices=TYPE_PRODUCT, attrs = {
                    'class':'form-control'
                }
            ),
            'model_product': forms.TextInput(
                attrs = {
                    'class':'form-control'
                    
                }
            ),
            'mac_address': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ejemplo: 00-aa-22-33-bb'
                }            
            ),
            'type_serial': forms.Select(
                choices=SERIAL_CHOICES, attrs = {
                    'class':'form-control'
                }
            ),
            'ram_pc': forms.Select(
                choices=RAM_CHOICES, attrs = {
                    'class':'form-control'
                }
            ),
            'ram_pc_type': forms.Select(
                choices=RAM_TYPE, attrs = {
                    'class':'form-control'
                }
            ),
            'disk_pc': forms.Select(
                choices=HARD_DISK_TYPE, attrs = {
                    'class':'form-control'
                }
            ),
             'disk_pc_type': forms.Select(
                choices=HARD_DISK, attrs = {
                    'class':'form-control'
                }
            ),
             'disk_pc_model': forms.Select(
                choices=HARD_DISK_MODEL, attrs = {
                    'class':'form-control'
                }
                
            ),
             'processor': forms.Select(
                choices=PROCESSOR_UNID, attrs = {
                    'class':'form-control'
                } 
            ),
            'processor_model': forms.TextInput(
                 attrs = {
                    'placeholder':'Ingrese modelo del Procesador',
                    'class':'form-control'
                } 
            ),
            'serial': forms.TextInput(
                attrs = {
                    'class':'form-control'
                }            
            ),
            'active_code': forms.TextInput(
                attrs = {
                    'class':'form-control'
                    
                }            
            ),
            'product_quantity': forms.NumberInput(
                attrs = {
                    'class':'form-control',
                    'readonly': True
                }            
            ),
            'warehouse': forms.Select(
                attrs = {
                    'class':'form-control'
                }
            ),
            'product_status': forms.Select(
                attrs = {
                    'class':'form-control'
                }
            ),
            'buy_product' : AdminDateWidget(
                attrs = {
                    'type':'date',
                    'class':'form-control'
                }
            )
        }
    