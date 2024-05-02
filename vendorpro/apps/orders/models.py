from django.db import models
from vendors.models import Vendor
from vendorpro.apps.utils import OrderStatus
from django_lifecycle import LifecycleModel, hook, BEFORE_UPDATE, AFTER_UPDATE
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

class PurchaseOrder(LifecycleModel):
    STATUS_CHOICES = (
        ("PENDING", "pending"),
        ("COMPLETED", "completed"),
        ("CANCELLED", "cancelled"),
    )
    po_number = models.CharField(max_length=100, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default="PENDING"
    )
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True)

    


