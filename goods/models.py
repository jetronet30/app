from statistics import quantiles
from unicodedata import category

from django.db import models
from django.db.models import (
    CharField,
    DecimalField,
    ForeignKey,
    PositiveIntegerField,
    SlugField,
    TextField,
)


class Categories(models.Model):
    name = CharField(max_length=150, unique=True, verbose_name="name")
    slug = SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )

    class Meta:
        db_table = "category"
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name


class Products(models.Model):
    name = CharField(max_length=150, verbose_name="name")
    slug = SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    discription = TextField(blank=True, null=True, verbose_name="discription")
    image = models.ImageField(
        upload_to="goods_images", blank=True, null=True, verbose_name="image"
    )
    price = DecimalField(
        default=0.00, max_digits=10, decimal_places=2, verbose_name="price"
    )
    discount = DecimalField(
        default=0.00, max_digits=10, decimal_places=2, verbose_name="discount"
    )
    quantity = PositiveIntegerField(default=0, verbose_name="quantity")
    category = ForeignKey(
        to=Categories, on_delete=models.PROTECT, verbose_name="category"
    )

    class Meta:
        db_table = "product"
        verbose_name = "product"
        verbose_name_plural = "products"

    def __str__(self):
        return self.name
    
    def display_id(self):
        return f"{self.id:05}" 
    
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price
