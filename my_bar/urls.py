from beers.views import RegisterView, StatisticsView
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

API_TITLE = "My bar"
API_DESCRIPTION = "My bar's API"
schema_view = get_schema_view(title=API_TITLE)
api_urlpatterns = [
    path("", include("beers.urls")),
    re_path(r"statistics", StatisticsView.as_view(), name="statistics"),
    # Auth/Token :
    path("auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("auth/register/", RegisterView.as_view(), name="auth_register"),
]
urlpatterns = [
    path("", RedirectView.as_view(url="/api/references", permanent=True)),
    re_path(r"^admin/", admin.site.urls),
    re_path(r"^api/", include(api_urlpatterns)),
    re_path(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    re_path(
        r"^api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    re_path(
        r"^api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
