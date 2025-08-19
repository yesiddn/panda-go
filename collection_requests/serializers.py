from rest_framework import serializers
from routes.serializers import CollectionRouteSerializer
from .models import Request
from waste_categories.serializers import WasteCategorySerializer
from waste_categories.models import WasteCategory

class RequestSerializer(serializers.ModelSerializer):
    waste_category = WasteCategorySerializer(read_only=True)
    waste_category_id = serializers.PrimaryKeyRelatedField(
        queryset=WasteCategory.objects.all(),
        write_only=True,
        source="waste_category",
        required=False,
        allow_null=True,
    )
    route = CollectionRouteSerializer(read_only=True)

    class Meta:
        model = Request
        fields = "__all__"
        read_only_fields = ("user", "status", "status_reason", "request_date", "route")
