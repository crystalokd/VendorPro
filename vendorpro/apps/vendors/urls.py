from django.urls import path, include
from .views import VendorViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()

router.register(r'vendors', VendorViewSet)

urlpatterns = router.urls
