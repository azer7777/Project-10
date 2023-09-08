from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework import permissions


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class IsContributor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user in obj.contributors.all()


class CanAccessProjectResources(permissions.BasePermission):
    message = "You do not have permission to access this resource."

    def has_permission(self, request, view):
        project = view.get_project_from_request(request)
        return project and project.contributors.filter(id=request.user.id).exists()
