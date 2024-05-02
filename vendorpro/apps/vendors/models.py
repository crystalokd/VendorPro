import uuid
from typing import Union

from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse

from vendorpro.utils.shortcuts import get_random_code


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Vendor(BaseModel):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(
        max_length=50, unique=True, default=get_random_code, editable=False
    )
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    class Meta:
        verbose_name = _("vendor")
        verbose_name_plural = _("vendors")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("vendors:vendor-actions", kwargs={"pk": self.pk})

    @property
    def on_time_delivery_rate(self):
        total_orders = self.purchaseorder_set.count()
        on_time_orders = self.purchaseorder_set.filter(
            delivery_date__lte=F('acknowledgment_date')
        ).count()
        return (on_time_orders / total_orders) * 100 if total_orders > 0 else 0











class HistoricalPerformance(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    history_date = models.DateTimeField(
        auto_now_add=True
    )  # the date field name is changed to history_date
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor.name} - {self.history_date}"

    class Meta:
        ordering = ["-history_date"]
        verbose_name = "Historical Performance"
        verbose_name_plural = "Historical Performances"