from django.db import models
from vendors.models import Vendor
from vendorpro.apps.utils import OrderStatus
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from vendorpro.utils.shortcuts import get_default_expected_delivery_date


class PurchaseOrder(models.Model):
    STATUS_CHOICES = (
        ("PENDING", "pending"),
        ("COMPLETED", "completed"),
        ("CANCELLED", "cancelled"),
    )
    po_number = models.CharField(max_length=100, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default="PENDING"
    )
    quality_rating = models.FloatField(null=True)

    order_date = models.DateTimeField()
    expected_delivery_date = models.DateTimeField(default=get_default_expected_delivery_date)
    actual_delivery_date = models.DateTimeField()

    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True)



@receiver(post_save, sender=PurchaseOrder)
def my_model_post_save_handler(sender, instance, created, **kwargs):
    if created:
        # Do something when a new instance of MyModel is created
        pass