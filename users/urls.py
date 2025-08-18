from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import UserRegistrationView, UserDetailView

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="user_registration"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),  # endpoint para verificar el token
    path("me/", UserDetailView.as_view(), name="user_detail"),
]
