from django.urls import path, include

from dish import views
urlpatterns = [
    path('newest-dishes/', views.NewestDishesList.as_view()),
    path('dishes/<slug:category_slug>/<slug:dish_slug>/',
         views.DishDetail.as_view()),
    path('dishes/<slug:category_slug>/', views.CategoryDetail.as_view()),
]
