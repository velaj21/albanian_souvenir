from django.contrib import admin
from .models import OrderedProduct


class ProductOrderedProduct(admin.TabularInline):
    model = OrderedProduct
    autocomplete_fields = ('product',)
    extra = 1
    ordering = ('product__name',)


