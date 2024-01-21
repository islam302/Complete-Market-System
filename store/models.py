from django.core.validators import MinValueValidator
from django.contrib import admin
from django.contrib.auth import settings
from django.db import models
from uuid import uuid4


class Customer(models.Model):
    MEMBERSHIP_CHOICES = [
        ('B', 'Bronze'),
        ('S', 'Silver'),
        ('G', 'Gold'),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    membership = models.CharField(choices=MEMBERSHIP_CHOICES, max_length=1, default='B')
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    orders = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(
        Customer, on_delete=models.PROTECT)


class Product(models.Model):
    name = models.CharField(max_length=35, verbose_name="product_name")
    price = models.DecimalField(max_digits=2, decimal_places=2, verbose_name="product_price")
    quantity = models.PositiveSmallIntegerField()
    country_of_origin = models.CharField(max_length=35)
    inventory = models.IntegerField(validators=[MinValueValidator(0)])
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)

    class Meta:
        ordering = ['name', 'price']


class Collection(models.Model):
    name = models.CharField(max_length=35, verbose_name="collection_name")
    products = models.ManyToManyField(Product, verbose_name='product')

    class Meta:
        ordering = ['name']


class Order(models.Model):

    PAYMENT_STATUS_CHOICES = [
        ('P', 'Pending'),
        ('C', 'Complete'),
        ('F', 'Failed')
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

    class Meta:
        permissions = [
            ('cancel_order', 'Can cancel order')
        ]


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name='orderitems')
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    cart_items = models.OneToOneField(CartItem, on_delete=models.CASCADE)


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.PROTECT, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)]
    )

    class Meta:
        unique_together = [['cart', 'product']]


class Review(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)


