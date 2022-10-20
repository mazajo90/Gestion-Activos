from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import DisplayPC, AsignationDisplay, AsignationDisplayHistory
from usuarios.models import User
from .forms import DisplayPCForm

class DisplayPCResource(resources.ModelResource):
    class Meta:
        model = DisplayPC

class DisplayAdmin( ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = [('created')]
    resources_class = DisplayPCResource
    search_fields =('display_name','display_size','display_tech', 'serial', 'asig_id')
    list_display    = ('display_name', 'display_size', 'display_tech')
    

class DisplayAsigResource(resources.ModelResource):
    class Meta:
        model = AsignationDisplay

class DisplayAsig( ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = [('asig_id')]
    search_fields = ('display_name__display_name', 'user__user_name', 'user__user_last_name', 'display_name__asig_id', 'display_name__serial')
    autocomplete_fields = ['display_name', 'user']
    
class AsignationDisplayHistoryResourse(resources.ModelResource):
    class Meta:
        model = AsignationDisplayHistory     

class AsignationDisplayHistoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display    = ('display_name', 'user')
    search_fields = ('display_name__display_name', 'user__user_name', 'user__user_last_name')
    autocomplete_fields = ['display_name', 'user']           
    
admin.site.register(DisplayPC,DisplayAdmin)
admin.site.register(AsignationDisplay, DisplayAsig)        
admin.site.register(AsignationDisplayHistory, AsignationDisplayHistoryAdmin)    
