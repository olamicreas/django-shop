from email.policy import default
from pydoc import describe
from unicodedata import category, name
from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    stock = models.CharField(max_length=300)
    colors = models.TextField()
    description = models.TextField()
    brand = models.ManyToManyField('Brand', related_name='brand')
    category = models.ManyToManyField('Category', related_name='category')
    image1 = models.ImageField(default='me.png', null=False, upload_to='product_pics')
    image2 = models.ImageField(default='me.png', null=False, upload_to='product_pics ')
    image3 = models.ImageField(default='me.png', upload_to='product_pics ')

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name
