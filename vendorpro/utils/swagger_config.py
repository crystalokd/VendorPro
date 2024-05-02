import os
from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title=f"{os.environ.get('APPLICATION_NAME', 'Vendor Pro')} API (CARD schema v1.2.0)",
        default_version='v1.0.0',
        description="API implementation of INGENIOUS",
        terms_of_service="#",
        contact=openapi.Contact(email="contact@e4email.net"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
