from django.contrib import admin
from . import models


# Register your models here.


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'image_tag')
    list_select_related = ('category', 'shop')
    readonly_fields = ('image_tag',)
    search_fields = ('name__istartswith', 'description__in')
    autocomplete_fields = ('category', 'shop')
    list_filter = ('category',)
    list_per_page = 80


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name__istartswith',)
    list_filter = ('name',)
    list_per_page = 80
