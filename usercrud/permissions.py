from rest_framework import permissions

class IsOwnUser(permissions.BasePermission):
    """
    Custom permission to only allow users to delete their own account.
    """

    def has_object_permission(self, request, view, obj):
        return obj == request.user