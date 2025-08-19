from django.urls import path
from .views import (
    CollectionRouteListCreateAPIView,
    CollectionRouteRetrieveUpdateDestroyAPIView,
    CollectionRouteSetInProgressAPIView,
    CollectionRouteSetCompletedAPIView,
)

urlpatterns = [
    path("", CollectionRouteListCreateAPIView.as_view(), name="route-list-create"),
    path(
        "<int:pk>/",
        CollectionRouteRetrieveUpdateDestroyAPIView.as_view(),
        name="route-detail",
    ),
    path(
        "<int:pk>/set-in-progress/",
        CollectionRouteSetInProgressAPIView.as_view(),
        name="route-set-in-progress",
    ),
    path(
        "<int:pk>/set-completed/",
        CollectionRouteSetCompletedAPIView.as_view(),
        name="route-set-completed",
    ),
]
