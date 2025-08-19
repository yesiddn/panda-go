from rest_framework import generics, permissions
from .models import Request
from .serializers import RequestSerializer
from .serializers import ApprovalSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group
from drf_spectacular.utils import extend_schema
from routes.models import CollectionRoute
from django.db.models import Count, F


class IsEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.groups.filter(name="employee").exists()
        )


class RequestListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = RequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Request.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Save the request and then try to assign an available route
        req = serializer.save(user=self.request.user)

        # If a route wasn't set during creation, try to find an available one
        if not req.route:
            available_route = (
                CollectionRoute.objects.annotate(num_requests=Count("requests"))
                .filter(
                    locality=req.locality,
                    waste_category=req.waste_category,
                    status="planned",
                    capacity_stops__gt=F("num_requests"),
                )
                .first()
            )

            if available_route:
                req.route = available_route
                req.status = "assigned"
                req.save()


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


class RequestApproveAPIView(generics.UpdateAPIView):
    """Allow users in the 'employee' group to approve a Request (set status to 'approved' and optional status_reason)."""

    serializer_class = ApprovalSerializer
    permission_classes = [IsEmployee]
    queryset = Request.objects.all()

    @extend_schema(request=ApprovalSerializer, responses=None)
    def patch(self, request, *args, **kwargs):
        req = self.get_object()
        serializer = self.get_serializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        status_reason = serializer.validated_data.get("status_reason")
        weight_kg = serializer.validated_data.get("weight_kg")
        req.status = "approved"
        if status_reason is not None:
            req.status_reason = status_reason
        if weight_kg is not None:
            req.weight_kg = weight_kg
        req.save(update_fields=["status", "status_reason", "weight_kg", "updated_at"])
        return Response(status=status.HTTP_200_OK)
