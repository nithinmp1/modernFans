from email.mime import image
from django.db import models
from django.utils.safestring import mark_safe

class Products(models.Model):
    prd_id = models.AutoField(primary_key=True)
    prd_name = models.CharField(max_length=255,default='')
    prd_description = models.TextField(default='')
    prd_currency = models.CharField(max_length=100,default='')
    prd_image = models.CharField(max_length=100,default='')
    prd_status = models.CharField(max_length=10,default='1')
    prd_image = models.ImageField(null=True,blank=True, upload_to='uploads/')
    prd_created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.prd_name

class Gallery(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Products,on_delete=models.CASCADE,blank=True,null=True)
    image = models.ImageField(null=True,blank=True, upload_to='upload/')
    meta = models.CharField(max_length=255,default='1')

    def image_tag(self):
        return mark_safe('<img src="{}" width="100" />'. format(self.image.url))
    image_tag.short_description = 'image'
    image_tag.allow_tag = True