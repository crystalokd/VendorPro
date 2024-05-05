import uuid
from typing import Union

from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse

from vendorpro.utils.shortcuts import get_random_code
from django.db.models import F, ExpressionWrapper, fields

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Vendor(models.Model):
    vendor_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
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
    
    def calc_on_time_delivery_rate(self):
        """
        Calculates the on-time delivery rate for the vendor based on expected delivery date.
        """
        completed_orders = self.purchaseorder_set.filter(status='COMPLETED')
        on_time_orders = completed_orders.filter(expected_delivery_date__lte=F('actual_delivery_date'))
        total_completed_orders = completed_orders.count()
        if total_completed_orders > 0:
            self.on_time_delivery_rate = on_time_orders.count() / total_completed_orders
        else:
            self.on_time_delivery_rate = 0.0
        self.save()

    def calc_quality_rating_avg(self):
        """
        Calculates the average quality rating given to the vendor's purchase orders.
        """
        total_orders = self.purchaseorder_set.filter(quality_rating__isnull=False).count()
        if total_orders > 0:
            quality_ratings = self.purchaseorder_set.filter(quality_rating__isnull=False).aggregate(total_quality_rating=models.Sum('quality_rating'))
            self.quality_rating_avg = quality_ratings['total_quality_rating'] / total_orders
        else:
            self.quality_rating_avg = 0.0
        self.save()

    def calc_average_response_time(self):
        """
        Calculates the average response time taken by the vendor to acknowledge or respond to purchase orders.
        """
        response_time = ExpressionWrapper(F('acknowledgment_date') - F('issue_date'), output_field=fields.DurationField())
        avg_response_time = self.purchaseorder_set.filter(acknowledgment_date__isnull=False).annotate(response_time=response_time).aggregate(avg_response_time=Avg('response_time'))
        if avg_response_time['avg_response_time'] is not None:
            self.average_response_time = avg_response_time['avg_response_time'].total_seconds() / 3600 # Convert to hours
        else:
            self.average_response_time = 0.0
        self.save()

    def calc_fulfillment_rate(self):
        """
        Calculates the fulfillment rate, percentage of purchase orders fulfilled without issues, for the vendor.
        """
        total_orders = self.purchaseorder_set.count()
        if total_orders > 0:
            fulfilled_orders = self.purchaseorder_set.filter(status='COMPLETED').count()
            self.fulfillment_rate = (fulfilled_orders / total_orders) * 100
        else:
            self.fulfillment_rate = 0.0
        self.save()












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