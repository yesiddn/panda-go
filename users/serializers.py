from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password


class UserRegistrationSerializer(serializers.ModelSerializer):
    role = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            "username", "password", "password2", "email", "first_name", "last_name", "role"
        )
        extra_kwargs = {
            "email": {"required": True}
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

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

        user = User.objects.create_user(
            **validated_data
        )

        group = Group.objects.get(name=role_name)
        user.groups.add(group)

        return user