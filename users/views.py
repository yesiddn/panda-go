from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from .serializers import UserRegistrationSerializer
from rest_framework.permissions import IsAuthenticated
from .serializers import UserDetailSerializer
from datetime import timedelta
from django.utils import timezone
from collection_requests.models import Request
from waste_categories.models import WasteCategory

User = get_user_model()

from datetime import timedelta
from django.utils import timezone
from collection_requests.models import Request
from waste_categories.models import WasteCategory

class UserRegistrationView(generics.CreateAPIView):
    """
    API view to create a new user.
    """
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        if user.groups.filter(name='user').exists():
            try:
                organic_category = WasteCategory.objects.get(name='Organico')
                collection_date = timezone.now().date() + timedelta(days=7)
                address_snapshot = {'address': user.locality.name}

                Request.objects.create(
                    user=user,
                    locality=user.locality,
                    waste_category=organic_category,
                    collection_date=collection_date,
                    address_snapshot=address_snapshot,
                )
            except WasteCategory.DoesNotExist:
                # Handle case where 'Organico' category does not exist
                pass

class UserDetailView(generics.RetrieveAPIView):
    """Return the authenticated user's data."""

    serializer_class = UserDetailSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
