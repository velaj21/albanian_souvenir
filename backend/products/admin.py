from django.contrib import admin
from . import models
from . import inlines
from django.db.models import Count


# Register your models here.


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'image_tag')
    list_select_related = ('category',)
    readonly_fields = ('image_tag',)
    search_fields = ('name__istartswith', 'description__in')
    autocomplete_fields = ('category',)
    list_filter = ('category',)
    list_per_page = 80


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name__istartswith',)
    list_filter = ('name',)
    list_display = ('id', 'name',)
    list_editable = ('name',)
    list_per_page = 80


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ('full_name__istartswith', 'email__istartswith', 'phone_number__istartswith')
    list_filter = ('is_confirmed',)
    list_display = ('full_name', 'email', 'phone_number', 'is_confirmed')
    list_per_page = 80
    inlines = [inlines.ProductOrderedProduct]
    readonly_fields = ('create_date', 'counted_products')

    def counted_products(self, request):
        counted_products = request.orderedproduct_set.all().filter(order__id=request.pk) \
            .values('product__name').annotate(count=Count('id')).values('product__name', 'count')
        return '\n'.join(('{} - {}'.format(item['count'], item['product__name'])) for item in counted_products)


@admin.register(models.OrderedProduct)
class OrderedProductAdmin(admin.ModelAdmin):
    search_fields = ('order', 'product')
    list_select_related = ('order', 'product')
    autocomplete_fields = ('order', 'product')
    list_per_page = 80
