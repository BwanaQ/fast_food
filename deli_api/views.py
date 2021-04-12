from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics, permissions,viewsets
from .serializers import LoginSerializer



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    # permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class LoginView(viewsets.ModelViewSet):

    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = LoginSerializer
    permission_classes = [permissions.IsAuthenticated]