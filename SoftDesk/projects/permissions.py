from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework import permissions
class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class IsContributor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the requesting user is among the project's contributors
        return request.user in obj.contributors.all()