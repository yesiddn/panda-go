from rest_framework import generics, permissions
from .models import CollectionRoute
from .serializers import CollectionRouteSerializer


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


class CollectionRouteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CollectionRouteSerializer
    permission_classes = [IsCompanyUser]

    def get_queryset(self):
        return CollectionRoute.objects.filter(company=self.request.user.company)