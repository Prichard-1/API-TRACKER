from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Custom permission: Only owners can edit/delete their activities.
    """
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
