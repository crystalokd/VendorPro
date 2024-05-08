from rest_framework import viewsets, status, generics
from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer
# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AcknowledgePurchaseOrderSerializer

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer



@api_view(['POST'])
def acknowledge_purchase_order(request, po_id):
    try:
        purchase_order = PurchaseOrder.objects.get(pk=po_id)
    except PurchaseOrder.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'POST':
        serializer = AcknowledgePurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            acknowledgment_date = serializer.validated_data.get('acknowledgment_date')
            purchase_order.acknowledgment_date = acknowledgment_date
            purchase_order.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



