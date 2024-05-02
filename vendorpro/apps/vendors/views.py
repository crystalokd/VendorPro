from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Vendor, HistoricalPerformance
from .serializers import VendorSerializer, HistoricalPerformanceSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def calc_on_time_delivery_rate(self) -> float:
        """
        The function calculates the on-time delivery rate by dividing the count of purchase orders by
        the count of purchase orders with acknowledgment dates before or on the delivery dates
        """
        po_list = self.get_purchase_orders_by_status(status=OrderStatus.COMPLETED)
        filter_on_time_deliverables = po_list.filter(
            acknowledgment_date__lte=models.F("delivery_date")
        )
        try:
            return round(filter_on_time_deliverables.count() / po_list.count(), 2)
        except ZeroDivisionError:
            return 0



    @action(detail=True, methods=["get"], url_path="performance")
    def performance(self, request, pk=None):
        vendor = self.get_object()
        performance_data = {
            "on_time_delivery_rate": vendor.on_time_delivery_rate,
            "quality_rating_avg": vendor.quality_rating_avg,
            "average_response_time": vendor.average_response_time,
            "fulfillment_rate": vendor.fulfillment_rate
        }
        return Response(performance_data, status=status.HTTP_200_OK)



class VendorPerformanceHistoryView(generics.ListAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer
