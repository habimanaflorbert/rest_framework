from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    Assumes the object has a `.owner` attribute.
    """
    message = "Something went wrong. You're not allowed to do this."
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request.
        if request.user.is_staff:
            # Write permissions are only allowed to the owner.
            return request.user.is_staff==True
        raise PermissionDenied(detail=self.message)
    
    def has_permission(self, request, view):
        # Read permissions are allowed to any request.
        if request.user.is_staff:
            # Write permissions are only allowed to the owner.
            return request.user.is_staff==True
        raise PermissionDenied(detail=self.message)