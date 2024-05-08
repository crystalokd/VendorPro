# vendor.tasks.py
from celery import shared_task
from vendors.models import Vendor
from .models import HistoricalPerformance
from datetime import datetime
@shared_task
def save_vendor_historical_performance():
    vendors = Vendor.objects.all()
    for vendor in vendors:
        # Calculate historical performance metrics here
        historical_performance = HistoricalPerformance(
            vendor=vendor,
            timestamp=datetime.now(),
            on_time_delivery_rate=vendor.calc_on_time_delivery_rate(),
            quality_rating_avg=vendor.calc_quality_rating_avg(),
            average_response_time=vendor.calc_average_response_time(),
            fulfillment_rate=vendor.calc_fulfillment_rate()
        )
        historical_performance.save()

        
@shared_task
def printsom():
    print("celery.......>>>")