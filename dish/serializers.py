from rest_framework import serializers

from .models import Category, Dish


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = (
            "id",
            "name",
            "description",
            "price",
            "get_image"
        )
