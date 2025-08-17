from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Locality
from .serializers import LocalitySerializer

class LocalityListView(generics.ListAPIView):
    queryset = Locality.objects.all()
    serializer_class = LocalitySerializer
    permission_classes = [AllowAny]