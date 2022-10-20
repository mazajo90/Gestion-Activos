from django import forms 
from django.contrib.admin.widgets import AutocompleteSelect, AdminDateWidget
from django.contrib import admin
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.core.exceptions import ValidationError
from django.template.loader import get_template
from .models import DisplayPC, AsignationDisplay
from .choices import TYPE_DISPLAY, INCH

from usuarios.models import User

class DisplayPCForm(forms.ModelForm):
    class Meta:
        model = DisplayPC
        fields = ['display_name', 'display_model', 'display_size', 'display_tech', 'active_code', 'display_quantity', 'warehouse', 'product_status', 'asig_id', 'serial', 'created']
        widgets= {
            'asig_id': forms.TextInput(
                attrs = {
                    'readonly': True,
                    'class':'form-control'
                }
            ),
            'serial': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese serial'
                }
            ),
            'display_name' : forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Escriba marca de Pantalla'
                }
            ),
            'display_model' : forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Modelo de Pantalla'
                }
            ),
            'display_size' : forms.Select(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Seleccione'
                }
            ),
            'display_tech' : forms.Select(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Seleccione'
                }
            ),
            'active_code': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese codigo'
                }
            ),
            'display_quantity': forms.NumberInput(
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
            'created' : AdminDateWidget(
                attrs = {
                    'type':'date',
                    'class':'form-control'
                }
            )
        }
        labels={
            'display_name': '',
            'display_model': '',
            'display_size':'',
            'display_tech':'',
            'active_code':''
        }

class AsignationDisplayForm(forms.ModelForm):
    class Meta:
        model = AsignationDisplay
        fields = ['asig_id','product_status', 'asignation_status', 'dep_boss', 'boss', 'acta_ent', 'user', 'display_name', 'display_name', 'date']
        
        widgets = {
            'date' : AdminDateWidget(
                attrs = {
                    'type':'date',
                    'class':'form-control'
                }
            ),
            'product_status': forms.Select(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Seleccione'
                }
            ),
            'asignation_status': forms.Select(
              attrs = {
                'class':'form-control'
              }  
            ),
            'dep_boss' : forms.Select(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'boss' : forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombre de Jefe a Cargo'
                }
            ),
            'acta_ent' : forms.Textarea(
                attrs = {
                    'placeholder': 'Ingrese observaciones'
                }
            ),
            'user': AutocompleteSelect(
                AsignationDisplay._meta.get_field('user'),
                admin.site,
                attrs = {
                    'class': 'form-control',
                    'placeholder':'Seleccione un Colaborador'
                }
            ),
            'display_name': AutocompleteSelect(
                AsignationDisplay._meta.get_field('display_name'),
                admin.site,
                attrs = {
                    'class': 'form-control'
                }
            ),
            'asig_id': forms.TextInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
        }
        labels={
            'acta_ent': ''
        }    
    def clean_display_name(self):
        display_name = self.cleaned_data['display_name']
        ex = AsignationDisplay.objects.filter(display_name=display_name).exists()
        if ex:
            raise ValidationError('Este articulo ya ha sido asignado a un colaborador')
        return display_name