import datetime

from django.contrib.auth.models import User

from django.db import models
from django.db.models import (
    Model, CharField, DecimalField, SmallIntegerField,
    SlugField, ForeignKey, CASCADE, PROTECT, TextField, DateField, IntegerField,
)


# 010826' adding the manager, delivery crew, customer

class Order(Model):
    account_number = CharField(max_length=12, unique=True, null=True)
    customer_name = CharField(max_length=100)
    address = TextField()
    phone = CharField(max_length=20)

    items = TextField()  # or JSONField if you prefer
    total = DecimalField(max_digits=8, decimal_places=2)

    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('preparing', 'Preparing'),
            ('out_for_delivery', 'Out for Delivery'),
            ('delivered', 'Delivered'),
        ],
        default='pending'
    )

    assigned_to = ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='delivery_orders'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"

