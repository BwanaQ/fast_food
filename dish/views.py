from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Dish
from .serializers import DishSerializer


class NewestDishesList(APIView):
    def get(self, request, format=None):
        dishes = Dish.objects.all()[0:4]
        serializer = DishSerializer(dishes, many=True)
        return Response(serializer.data)


class DishDetail(APIView):
    def get_object(self, category_slug, dish_slug):
        try:
            return Dish.objects.filter(category__slug=category_slug).get(slug=dish_slug)
        except Dish.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, product_slug,  format=None):
        dish = self.get_object(category_slug, product_slug)
        serializer = DishSerializer(dish)
        return Response(serializer.data)
