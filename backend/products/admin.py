from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'image_tag')
    readonly_fields = ('image_tag',)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
