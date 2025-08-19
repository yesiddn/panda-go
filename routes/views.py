from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import CollectionRoute
from .serializers import CollectionRouteSerializer
from drf_spectacular.utils import extend_schema, OpenApiResponse


class IsCompanyUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.company is not None


class CollectionRouteListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CollectionRouteSerializer
    permission_classes = [IsCompanyUser]

    def get_queryset(self):
        return CollectionRoute.objects.filter(company=self.request.user.company)

    def perform_create(self, serializer):
        serializer.save(company=self.request.user.company)


class CollectionRouteRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    serializer_class = CollectionRouteSerializer
    permission_classes = [IsCompanyUser]

    def get_queryset(self):
        return CollectionRoute.objects.filter(company=self.request.user.company)


class CollectionRouteSetInProgressAPIView(APIView):
    """Set the route status to 'in_progress' using only the PK in the URL (no request body required).

    Using APIView avoids DRF schema generators inferring a request body from a serializer_class.
    """

    permission_classes = [IsCompanyUser]

    @extend_schema(request=None, responses=CollectionRouteSerializer)
    def post(self, request, pk, *args, **kwargs):
        queryset = CollectionRoute.objects.filter(company=request.user.company)
        route = get_object_or_404(queryset, pk=pk)
        route.status = "in_progress"
        route.save(update_fields=["status", "updated_at"])
        serializer = CollectionRouteSerializer(route, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class CollectionRouteSetCompletedAPIView(APIView):
    """Set the route status to 'completed' using only the PK in the URL (no request body required)."""

    permission_classes = [IsCompanyUser]

    @extend_schema(request=None, responses=CollectionRouteSerializer)
    def post(self, request, pk, *args, **kwargs):
        queryset = CollectionRoute.objects.filter(company=request.user.company)
        route = get_object_or_404(queryset, pk=pk)
        route.status = "completed"
        route.save(update_fields=["status", "updated_at"])
        serializer = CollectionRouteSerializer(route, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)
