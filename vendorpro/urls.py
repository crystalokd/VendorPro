
from django.contrib import admin
from django.urls import path, include

import os
from django.conf.urls.static import static
from django.conf import settings


from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from vendorpro.utils.swagger_config import schema_view


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from dotenv import load_dotenv
load_dotenv()

urlpatterns = [
    path('admin/', admin.site.urls),

    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    path('', include('vendors.urls')),
    path('', include('orders.urls')),
]


