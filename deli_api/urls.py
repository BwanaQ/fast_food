from django.urls import path
from . import views


urlpatterns = [
    # to be removed
    path('', views.HelloView.as_view(), name='hello'),
]
