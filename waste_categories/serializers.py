from rest_framework import serializers
from .models import WasteCategory

class WasteCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WasteCategory
        fields = '__all__'
