from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.db import models

from .models import Phone

class PhoneResource(resources.ModelResource):
    class Meta:
        model = Phone

class PhoneAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = [('phone_quantity')]
    resources_class = PhoneResource
    search_fields   = (
        'phone_id',
        'phone_name',
        'phone_model',
        'phone_imei1',
        'phone_imei2',
        'phone_serial'
    )
    list_display    = (
        'phone_id',
        'phone_name',
        'phone_model',
        'phone_imei1',
        'phone_imei2',
        'phone_serial'
    )

admin.site.register(Phone, PhoneAdmin)