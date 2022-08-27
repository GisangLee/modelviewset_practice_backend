import os
from rest_framework import permissions
from rest_framework.authentication import BasicAuthentication

class AllowAny(permissions.BasePermission):

    def has_permission(self, request, view):
        return True