from django.contrib import admin

from vendors.models import Vendor


class VendorAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = [
        "name",
        "vendor_code",
        "on_time_delivery_rate",
        "quality_rating_avg",
        "average_response_time",
        "fulfillment_rate",
    ]


admin.site.register(Vendor, VendorAdmin)
