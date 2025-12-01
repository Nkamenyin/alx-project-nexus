from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.http import HttpResponse

schema_view = get_schema_view(
    openapi.Info(
        title="ALX Project Nexus API",
        default_version='v1',
        description="API documentation for your project",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

#Home page
def home(request):
    return HttpResponse("Welcome to ALX Project Nexus By Valentine Eyet!")

urlpatterns = [
    path('', home, name='home'),     #Home url
    path('admin/', admin.site.urls),

    # API ROUTES
    path('api/auth/', include('accounts.urls')),
    path('api/store/', include('store.urls')),

    # JWT AUTH
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    
    # SWAGGER DOCUMENTATION
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),

    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
]
