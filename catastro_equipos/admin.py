from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.db import models
from .models import  Product, ProductStatus

class ProductResource(resources.ModelResource):
    
    class Meta:
        model = Product

class NodoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = [('product_quantity')]
    resources_class = ProductResource
    search_fields = ('product_name','model_product', 'mac_address', 'active_code', 'type_product', 'serial')
    list_display = ('product_name','model_product', 'mac_address', 'active_code')



admin.site.register(Product, NodoAdmin)
admin.site.register(ProductStatus)

