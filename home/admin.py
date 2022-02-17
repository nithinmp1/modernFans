from dataclasses import field
from django.contrib import admin

from home.models import Gallery, Products
# Register your models here.

class ProductsListAdmin(admin.ModelAdmin):
    list_display = ('prd_id','prd_name','prd_image','prd_description')

class GalleryListAdmin(admin.ModelAdmin):
    field = ('product','image_tag','meta')
    list_display = ('product','image_tag','meta')
    readonly_fields =  ['image_tag']
    filter = ['product']
admin.site.register(Products,ProductsListAdmin)


admin.site.register(Gallery,GalleryListAdmin)