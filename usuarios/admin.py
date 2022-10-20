from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.db import models
from .models import User
from django.conf import settings

class UserResource(resources.ModelResource):
    
    class Meta:
        model = User

class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resources_class = UserResource
    search_fields = ('user_name', 'user_last_name','user_email', 'user_name_corp', 'is_activate')
    list_display = ('user_name', 'user_last_name', 'user_email', 'user_name_corp')
    list_per_page = settings.LIST_PER_PAGE
    

class Media:
        css = {
            'all': ('core/css/custom_ckeditor.css',)
        }
admin.site.register(User, UserAdmin)

