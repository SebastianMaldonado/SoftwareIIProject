<<<<<<< HEAD
from rest_framework import permissions

class IsOwnUser(permissions.BasePermission):
    """
    Custom permission to only allow users to delete their own account.
    """

    def has_object_permission(self, request, view, obj):
=======
from rest_framework import permissions

class IsOwnUser(permissions.BasePermission):
    """
    Custom permission to only allow users to delete their own account.
    """

    def has_object_permission(self, request, view, obj):
>>>>>>> c3d906adf9a22d9e79e87824df9b9fb4eb51a036
        return obj == request.user