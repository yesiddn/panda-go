from django.urls import path
from .views import (
    CollectionRouteListCreateAPIView,
    CollectionRouteRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path("", CollectionRouteListCreateAPIView.as_view(), name="route-list-create"),
    path(
        "<int:pk>/",
        CollectionRouteRetrieveUpdateDestroyAPIView.as_view(),
        name="route-detail",
    ),
]
