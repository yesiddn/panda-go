from rest_framework import serializers
from .models import CollectionRoute


class CollectionRouteSerializer(serializers.ModelSerializer):
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
