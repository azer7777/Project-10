from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrAdmin
from .models import CustomUser
from .serializers import UserSerializer, UserRegistrationSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer


