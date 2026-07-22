"""
Serializers for the user API View
"""

from django.contrib.auth import (
    get_user_model,
    authenticate,
)

from django.utils.translation import gettext as _

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user obhject."""

    class Meta:
        model = get_user_model()
        fields = [
            "email",
            "name",
            "password",
        ]  # only fields provided in the API request
        extra_kwargs = {
            "password": {"write_only": True, "min_length": 5}
        }  # write_only ensures the value is no returned

    # Only gets called if validation passed
    def create(self, validated_data):
        """Create and return a user with encryted password."""
        # This ensures we are using the customized version
        return get_user_model().objects.create_user(**validated_data)


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user auth token."""

    email = serializers.EmailField()
    password = serializers.CharField(
        style={"input": "password"},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        """Validate and authenticate the user."""
        email = attrs.get("email")
        password = attrs.get("password")
        user = authenticate(
            request=self.context.get("request"),
            username=email,
            password=password,
        )
        if not user:
            msg = _("Unable to authenticate with provided credentials")
            raise serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs
