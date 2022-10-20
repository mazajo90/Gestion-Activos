from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Asignation, AsignationState, AsignationHistory
from catastro_equipos.models import Product, ProductStatus
from .forms import AsignationForm
from django.conf import settings


class AsignacionResource(resources.ModelResource):
    class Meta:
        model = Asignation


class AsigAdmin( ImportExportModelAdmin, admin.ModelAdmin ):
    readonly_fields = ['asig_id']
    resources_class = AsignacionResource
    search_fields   = ('asig_id', 'date', 'dp_boss', 'boss', 'acta_ent', 'product__product_name', 'user__user_name', 'user__user_last_name', 'product__active_code', 'product__serial' )
    autocomplete_fields = ['product', 'user']
    list_display    = ('asig_id', 'user','date', 'dp_boss', 'boss', 'acta_ent')
    form = AsignationForm
    #list_per_page = settings.LIST_PER_PAGE

        
    
class AsigAdminStateResource( resources.ModelResource):
    class Meta:
        model = AsignationState
                
    
class AsigAdminHistoryResource( resources.ModelResource):
    class Meta:
        model = AsignationHistory
        
class AsigAdminHistory(ImportExportModelAdmin, admin.ModelAdmin):
    #readonly_fields = ('date_init', 'date_fin')
    resources_class = AsigAdminHistoryResource
    search_fields   = ('asig_id', 'product__product_name', 'user__user_name')
    autocomplete_fields = ['product', 'user']
    list_display    = ('asig_id', 'product', 'user', 'date_init', 'date_fin')
    list_per_page = settings.LIST_PER_PAGE           


admin.site.register(Asignation, AsigAdmin),
admin.site.register(AsignationState),
admin.site.register(AsignationHistory, AsigAdminHistory)

