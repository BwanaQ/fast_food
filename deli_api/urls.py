from django.urls import path, include
from .views import RegisterView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.LoginView)

urlpatterns = [
    # path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    # path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))    

]
