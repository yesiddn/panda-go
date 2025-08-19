from django.urls import path
from .views import (
    RequestListCreateAPIView,
    RequestRetrieveUpdateDestroyAPIView,
    RequestsByRouteAPIView,
    RequestApproveAPIView,
)

urlpatterns = [
    path("requests/", RequestListCreateAPIView.as_view(), name="request-list-create"),
    path(
        "requests/<int:pk>/",
        RequestRetrieveUpdateDestroyAPIView.as_view(),
        name="request-retrieve-update-destroy",
    ),
    path(
        "requests/route/<int:route_id>/",
        RequestsByRouteAPIView.as_view(),
        name="requests-by-route",
    ),
    path(
        "requests/<int:pk>/approve/",
        RequestApproveAPIView.as_view(),
        name="request-approve",
    ),
]
