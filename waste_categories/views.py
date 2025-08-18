from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import WasteCategory
from .serializers import WasteCategorySerializer

class WasteCategoryListView(generics.ListAPIView):
    queryset = WasteCategory.objects.all()
    serializer_class = WasteCategorySerializer
    permission_classes = [AllowAny]