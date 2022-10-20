from django.conf import settings
from django.contrib.admin.widgets import AdminDateWidget 
from django import forms 

from .models import Phone
from catastro_equipos.choices import PRODUCT_STATUS, PHONE_CHOICES, PHONE_TYPE

class PhoneForm(forms.ModelForm):
    model = Phone
    fields = [
        'phone_id',
        'phone_type',
        'phone_name',
        'phone_model',
        'phone_imei1',
        'phone_imei2',
        'phone_serial',
        'phone_status',
        'phone_created',
        'phone_number',
        'phone_quantity',
        'phone_buy'
    ]
    
    widgets = {
        'phone_id': forms.TextInput(
            attrs = {
                'class': 'form-control',
                'readonly': True
            }
        ),
        'phone_type':forms.Select(
            choices=PHONE_CHOICES, 
            attrs = {
                'class':'form-control'    
            }
        ),
        'phone_name': forms.Select(
            choices=PHONE_TYPE, 
            attrs = {
                'class': 'form-control'
            }
        ),
        'phone_model': forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Samsung'
            }
        ),
        'phone_imei1': forms.NumberInput(
            attrs = {
                'class':'form-control',
            }
        ),
        'phone_imei2': forms.NumberInput(
            attrs = {
                'class':'form-control',
            }
        ),
        'phone_serial': forms.TextInput(
            attrs = {
                'class': 'form-control'
            }
        ),
        'phone_status': forms.Select(
            choices=PRODUCT_STATUS,
            attrs = {
                'class': 'form-control'
            }
        ),
        'phone_created': AdminDateWidget(
            attrs = {
                'class': 'form-control',
                'type': 'date'
            }
        ),
        'phone_number': forms.NumberInput(
          attrs = {
              'class': 'form-control'
          }  
        ),
        'phone_quantity': forms.NumberInput(
            attrs = {
                'class': 'form-control',
                'readonly': True
            }
        ),
        'phone_buy': AdminDateWidget(
                attrs = {
                    'type':'date',
                    'class':'form-control'
                }
        )
    }