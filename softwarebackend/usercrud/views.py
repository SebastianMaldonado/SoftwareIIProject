from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer
from .models import UserProfile
# Create your views here.

from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .permissions import IsOwnUser

from rest_framework.permissions import IsAuthenticated

class UserProfileViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserProfile.objects.all()
    
    def get_permissions(self):
        """
        Allow the `IsAuthenticated` permission for all actions,
        and the `IsOwnUser` permission only for DELETE actions.
        """
        if self.action == 'create': 
            self.permission_classes = []
        if self.action == 'destroy':  # DELETE
            self.permission_classes = [IsOwnUser]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()