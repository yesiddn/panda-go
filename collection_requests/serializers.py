from rest_framework import serializers
from routes.serializers import CollectionRouteSerializer
from .models import Request
from waste_categories.serializers import WasteCategorySerializer
from waste_categories.models import WasteCategory
from users.serializers import UserDetailSerializer


class RequestSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    waste_category = WasteCategorySerializer(read_only=True)
    weight_kg = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )
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


class ApprovalSerializer(serializers.Serializer):
    """Serializer for approving a Request: only status_reason can be provided."""

    status_reason = serializers.CharField(
        required=False, allow_blank=True, allow_null=True
    )
    weight_kg = serializers.DecimalField(
        max_digits=10, decimal_places=2, required=False, allow_null=True
    )
