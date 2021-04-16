from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Dish, Category
from .serializers import DishSerializer, CategorySerializer


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

    def get(self, request, category_slug, dish_slug,  format=None):
        dish = self.get_object(category_slug, dish_slug)
        serializer = DishSerializer(dish)
        return Response(serializer.data)


class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


@api_view(['POST'])
def search(request):
    query = request.data.get('query',)
    if query:
        dishes = Dish.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query))
        serializer = DishSerializer(dishes, many=True)
        return Response(serializer.data)
    else:
        return Response({"dishes": []})
