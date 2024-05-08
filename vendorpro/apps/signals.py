# Import necessary modules
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from datetime import timedelta
from orders.models import PurchaseOrder
from vendors.models import Vendor
from django.db.models import F, Avg, ExpressionWrapper



# Signal receiver to update vendor performance metrics
@receiver(pre_save, sender=PurchaseOrder)
def update_vendor_performance(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = PurchaseOrder.objects.get(pk=instance.pk)
            if old_instance.status != instance.status:
                vendor = instance.vendor
                if vendor:
                    vendor.calc_fulfillment_rate()
        except PurchaseOrder.DoesNotExist:
            pass   
    
    vendor = instance.vendor
    if vendor:
        if instance.status == 'COMPLETED':
            vendor.calc_on_time_delivery_rate()
            if instance.quality_rating is not None:
                vendor.calc_quality_rating_avg()
        else:  # For statuses other than 'COMPLETED', calculate average response time
            if instance.acknowledgment_date is not None:
                vendor.calc_average_response_time()
