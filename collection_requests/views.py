from rest_framework import generics, permissions
from .models import Request
from .serializers import RequestSerializer


class RequestListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = RequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Request.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RequestRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Request.objects.filter(user=self.request.user)


class RequestsByRouteAPIView(generics.ListAPIView):
    """List requests associated to a given collection route id.

    Any authenticated user can access this endpoint.
    """

    serializer_class = RequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        route_id = self.kwargs.get("route_id")
        return Request.objects.filter(route__id=route_id)
