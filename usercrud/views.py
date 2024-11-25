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
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status

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
        elif self.action == 'destroy':  # DELETE
            self.permission_classes = [IsOwnUser]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
    
    def get_queryset(self):
        """
        Filter the queryset to only include the UserProfile of the authenticated user.
        """
        user = self.request.user
        if not user.is_authenticated:
            raise PermissionDenied("You must be logged in to view your profile.")
        
        return UserProfile.objects.filter(user=user)

    def retrieve(self, request, *args, **kwargs):
        """
        Override retrieve to ensure the user can only retrieve their own profile.
        """
        user_profile = self.get_queryset().first()
        if not user_profile:
            raise PermissionDenied("No profile exists for the authenticated user.")
        
        serializer = self.get_serializer(user_profile)
        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        """
        Handle partial update (PATCH) request for a user profile.
        """
        # Get the user profile to update
        user_profile = self.get_queryset().first()

        if not user_profile:
            return Response({"detail": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)

        # Serialize and update the profile with the provided data
        serializer = self.get_serializer(user_profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()  # Save the updated profile
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, *args, **kwargs):
        """
        Handle DELETE request to delete a user profile.
        """
        # Get the user profile to delete
        user_profile = self.get_queryset().first()

        if not user_profile:
            return Response({"detail": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)

        # Delete the user profile
        user_profile.delete()
        return Response({"detail": "Profile deleted successfully"}, status=status.HTTP_204_NO_CONTENT)