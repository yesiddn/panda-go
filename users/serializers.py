from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from localities.models import Locality

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    role = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)
    locality_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)

    class Meta:
        model = User
        fields = (
            "username", "password", "password2", "email", "first_name", "last_name", "role", "locality_id"
        )
        extra_kwargs = {
            "email": {"required": True}
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        
        role = attrs.get("role")
        locality_id = attrs.get("locality_id")

        if role == "user" and not locality_id:
            raise serializers.ValidationError(
                {"locality_id": "Locality is required for users with role 'user'."}
            )

        return attrs
    
    def validate_locality_id(self, value):
        """
        Valida que la localidad enviada exista en la base de datos.
        """
        if value and not Locality.objects.filter(id=value).exists():
            raise serializers.ValidationError(f"Locality with id '{value}' does not exist.")
        return value

    def validate_role(self, value):
        """
        Valida que el rol (Grupo) enviado exista en la base de datos.
        """
        if not Group.objects.filter(name=value).exists():
            raise serializers.ValidationError(f"Role '{value}' does not exist.")
        return value

    def create(self, validated_data):
        role_name = validated_data.pop("role")
        validated_data.pop("password2")
        locality_id = validated_data.pop("locality_id", None)

        user = User.objects.create_user(
            **validated_data,
            locality_id=locality_id
        )

        group = Group.objects.get(name=role_name)
        user.groups.add(group)

        return user