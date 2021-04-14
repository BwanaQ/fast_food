from rest_framework import serializers

from .models import Category, Dish


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image"
        )


class CategorySerializer(serializers.ModelSerializer):
    dishes = DishSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "dishes",

        )
