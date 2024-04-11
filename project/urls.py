from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from project.api.viewsets.user_viewsets import user_by_credentials


urlpatterns = [path("admin/", admin.site.urls)]
urlpatterns += [
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns += [
    path("api/", include("players.urls"), name="players"),
    path("api/", include("games.urls"), name="games"),
    
    path("api/me/", user_by_credentials, name="me"),
]
