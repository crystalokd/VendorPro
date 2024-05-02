from django.urls import path, include
from .views import PurchaseOrderViewSet
from rest_framework.routers import SimpleRouter
from .views import acknowledge_purchase_order

router = SimpleRouter()

router.register(r'purchase_order', PurchaseOrderViewSet)


urlpatterns = [
    path('api/purchase_orders/<int:po_id>/acknowledge/', acknowledge_purchase_order),
] + router.urls