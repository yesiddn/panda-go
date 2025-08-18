from rest_framework import serializers
from .models import Company
from waste_categories.models import WasteCategory
from waste_categories.serializers import WasteCategorySerializer

class CompanySerializer(serializers.ModelSerializer):
    waste_categories = WasteCategorySerializer(many=True, read_only=True)
    waste_category_ids = serializers.PrimaryKeyRelatedField(
        queryset=WasteCategory.objects.all(),
        many=True,
        write_only=True,
        source='waste_categories'
    )

    class Meta:
        model = Company
        fields = ('id', 'name', 'waste_categories', 'waste_category_ids')