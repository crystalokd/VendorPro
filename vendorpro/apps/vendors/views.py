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
