from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

class IsAuthorOrReadOnly(BasePermission):
    """
    Custom permission to only allow authors to modify or delete a resource.
    Others can read the resource.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
