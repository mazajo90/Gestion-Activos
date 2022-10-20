from django import forms
from django.contrib.admin.widgets import AdminDateWidget 
from django.contrib import admin
from .models import User
from .choices import COMPANIES, DEPARTMENT_CHOISE, USER_STATUS
from asignacion.choices import DP_BOSS

from phonenumber_field.formfields import PhoneNumberField

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
        'id_user',    
        'user_name', 
        'user_last_name',
        'user_email',
        'user_phone',
        'user_name_corp',
        'user_corp',
        'user_status',
        'deparment_site',
        'boss_user_dep',
        'date',
        'boss_user',
        'dp_boss'
        ]
        widgets= {
            'id_user': forms.TextInput(
              attrs = {
                  'class':'form-control',
                  'readonly': True
              }  
            ),
            'user_name': forms.TextInput(
                attrs = {
                    'class':'form-control'
                }
            ),
            'user_last_name': forms.TextInput(
                attrs = {
                    'class':'form-control'
                }
            ),
            'user_email': forms.TextInput(
                attrs = {
                    'class':'form-control'
                }
            ),
            'user_phone': forms.NumberInput(
                attrs = {
                  'class':'form-control',
                  'placeholder': '912345678'
              }  
            ),
            'user_name_corp': forms.TextInput(
                attrs = {
                    'class':'form-control'
                }
            ),
            'user_corp': forms.Select(
                choices = COMPANIES,
                attrs = {
                    'class':'form-control'
                }
            ),
            'boss_user': forms.TextInput(
              attrs = {
                  'class':'form-control',
                  'placeholder': 'Nombre de Jefe'
              }  
            ),
            'dp_boss': forms.Select(
                choices = DP_BOSS,
                attrs = {
                    'class':'form-control'
                }
            ),
            'boss_user_dep': forms.Select(
                choices = DEPARTMENT_CHOISE,
                attrs = {
                    'class':'form-control'
                }
            ),
            'user_status': forms.Select(
                choices = USER_STATUS,
                attrs = {
                    'class':'form-control'
                    
                }
            ),
            'deparment_site': forms.TextInput(
                attrs = {
                    'class':'form-control'
                }
            ),
            'date': AdminDateWidget(
                attrs = {
                    'type':'date',
                    'class':'form-control'
                }
            )
        }
        
             
        