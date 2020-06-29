from rest_framework import permissions


SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']

class SafeMethodsPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.user and request.user.is_authenticated:
            return True
        return False