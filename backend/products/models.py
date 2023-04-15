from django.db import models
from django.core.validators import FileExtensionValidator, MinValueValidator
from django.utils.html import mark_safe


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['-name']


class Order(models.Model):
    full_name = models.CharField(max_length=35)
    email = models.EmailField(max_length=35)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    total_price = models.FloatField()
    is_confirmed = models.BooleanField()
    create_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'{self.full_name} {self.phone_number}'

    class Meta:
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=25)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    quantity = models.PositiveSmallIntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])])
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def image_tag(self):
        return mark_safe('<img src=\'{}\' width=\'150\' height=\'150\'/>'.format(self.image.url))

    image_tag.short_description = 'Product Image'
    image_tag.allow_tags = True

    def __str__(self):
        return f'{self.name} / {self.category}'

    class Meta:
        ordering = ['id']


class OrderedProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.order} / {self.product}'
