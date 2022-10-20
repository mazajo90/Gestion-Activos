from django.forms import HiddenInput, Form, CharField
from django.contrib import admin
from django.contrib.admin import ModelAdmin, SimpleListFilter
from django.contrib.admin.widgets import AutocompleteSelect, AdminDateWidget
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.db import models
from .models import Infraestructure
from django.conf import settings



class InfraestructureResource(resources.ModelResource):
    
    class Meta:
        model = Infraestructure
        
class InfraFilter(SimpleListFilter):
    title = 'Usuarios Activos'
    parameter_name = 'Infraestructure_active_ssh_user'
    
    
    def lookups(self, request, model_admin):
        return (
            ('Activo', 'Activo'),
            ('Deshabilitado', 'Deshabilitado')
        )
    
    def queryset(self, request, queryset):
        if self.value() == 'Activo':
            return queryset.exclude(active_ssh_user=False)
        if self.value() == 'Deshabilitado':
            return queryset.exclude(active_ssh_user=True)

           
                
class InfraestructureAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resources_class = InfraestructureResource
    search_fields   = ('ssh_user', 'active_ssh_user', 'user_ssh__user_name', 'user_ssh__user_last_name')
    list_display    = ('user_ssh','sub_area','job_area','ssh_user','ssh_key','ssh_password', 'active_ssh_user', 'created')
    autocomplete_fields = ['user_ssh']
    list_per_page   = settings.LIST_PER_PAGE
    list_filter = ['created', 'job_area', InfraFilter] 

         
class Media:
        css = {
            'all': ('core/css/custom_ckeditor.css')
        }
admin.site.register(Infraestructure, InfraestructureAdmin)
            

