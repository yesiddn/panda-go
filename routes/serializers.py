from rest_framework import serializers
from companies.serializers import CompanySerializer
from localities.models import Locality
from localities.serializers import LocalitySerializer
from .models import CollectionRoute
from waste_categories.serializers import WasteCategorySerializer

class CollectionRouteSerializer(serializers.ModelSerializer):
    waste_category = WasteCategorySerializer(read_only=True)
    company = CompanySerializer(read_only=True)
    locality = LocalitySerializer(read_only=True)
    locality_id = serializers.PrimaryKeyRelatedField(
        queryset=Locality.objects.all(),
        write_only=True,
        source="locality",
        required=False,
        allow_null=True,
    )

    class Meta:
        model = CollectionRoute
        fields = "__all__"
        read_only_fields = ("company",)

    def validate_waste_category(self, value):
        user = self.context["request"].user
        if not user.company:
            raise serializers.ValidationError(
                "El usuario no está asociado a ninguna empresa."
            )
        if value not in user.company.waste_categories.all():
            raise serializers.ValidationError(
                "La categoría de residuos no es válida para la empresa del usuario."
            )
        return value
