from django import forms
from django.contrib.admin.widgets import AutocompleteSelect, AdminDateWidget 
from django.contrib import admin
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.core.exceptions import ValidationError
from django.template.loader import get_template
from .models import Asignation, AsignationState
from catastro_equipos.models import Product, ProductStatus
from usuarios.models import User
from django.db.models import Q
from .choices import DP_BOSS, ASIGN_STATUS


class AsignationForm(forms.ModelForm):
    
    class Meta:
        model = Asignation
        fields = ['asig_id', 'dp_boss', 'boss', 'acta_ent', 'product', 'user', 'product_status', 'id_asig_status', 'date']
        widgets = {
            'asig_id' : forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'readonly' : True
                }
            ),
            'id_asig_status': forms.Select(
              attrs = {
                  'class':'form-control'
              }  
            ),
            'product_status': forms.Select(
                attrs = {
                    'class': 'form-control border_selector',
                    'placeholder': 'Seleccione'
                }
            ),
            'dp_boss' : forms.Select(
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
            'product' : AutocompleteSelect(
                Asignation._meta.get_field('product'),
                admin.site,
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Seleccione el Notebook'
                }
            ),
            'user': AutocompleteSelect(
                Asignation._meta.get_field('user'),
                admin.site,
                attrs = {
                    'class': 'form-control',
                    'placeholder':'Seleccione un Colaborador'
                }
            ),
            'date' : AdminDateWidget(
                attrs = {
                    'type':'date',
                    'class':'form-control'
                }
            )
            
        }
        labels = {
            'acta_ent': ''
        }    
        
    def clean_product(self):
        product = self.cleaned_data['product']
        ex = Asignation.objects.filter(product=product).exists()
        if self.instance:
            ex = Asignation.objects.filter(product=product).exclude(pk=self.instance.pk)
        if ex:
            raise ValidationError('Este articulo ya ha sido asignado a un colaborador')
        return product

            
    def send(self):
        subject = 'Asignación de Activo'
        template = get_template('asignacion/send_email.html')
        content = template.render({
            'self': self
        })
        msg = EmailMultiAlternatives(
                'Notificacion de Activos BCN',
                'Hola, queremos notificar que un equipo ha sido asignado, para mas informacion contacte al administrador',
                settings.EMAIL_HOST_USER,
                ['mazajo90@test.com']
        )
        msg.attach_alternative( content, 'text/html')
        msg.send()
        
            