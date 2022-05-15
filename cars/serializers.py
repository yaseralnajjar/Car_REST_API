from rest_framework import serializers
from cars.models import Car
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "password",
            "date_joined",
            "is_superuser",
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }
        read_only_fields = ["id", "date_joined", "is_superuser"]

    def create(self, validated_data):
        username = validated_data.get("username")
        validated_data["email"] = f"{username}@email.com"
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


class CarSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Car
        fields = ["url", "id", "user", "model", "brand", "color", "horsepower", "added"]
        read_only_fields = ["id", "user", "added"]

    def get_url(self, obj):
        return obj.get_api_url()

    # walidacja czy taki model istnieje + wykluczenie siebie samego z queryset
    def validate_model(self, value):
        queryset = Car.objects.filter(model__iexact=value)
        if self.instance:
            queryset = queryset.exclude(id=self.instance.id)
        if queryset.exists():
            raise serializers.ValidationError("The model of car has already been used!")
        return value
