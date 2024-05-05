from django.urls import path, include
from .views import PurchaseOrderViewSet, PurchaseOrderAcknowledgeView
from rest_framework.routers import SimpleRouter
from .views import acknowledge_purchase_order

router = SimpleRouter()

router.register(r'purchase_order', PurchaseOrderViewSet)


urlpatterns = [
    path('purchase_order/<int:po_id>/acknowledge/', acknowledge_purchase_order),
    path("<uuid:pk>/acknowledge", PurchaseOrderAcknowledgeView.as_view(), name="purchase-order-acknowledge"),
] + router.urls