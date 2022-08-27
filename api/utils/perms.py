import os
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from accounts import models as account_models
from utils.errors import Error

class AllowAny(permissions.BasePermission):

    def has_permission(self, request, view):
        return True



def owner_only(func):

    def wrapper_func(*args, **kwargs):

        print(args)
        print(kwargs)

        request = args[0]

        #logged_in_user = request.user
        logged_in_user = account_models.User.objects.get(pk = 5)
        target_id = kwargs.get("pk")

        if int(logged_in_user.id) != int(target_id):
            return Response(Error.errors("권한이 없습니다"), status=status.HTTP_401_UNAUTHORIZED)

        return func(*args, **kwargs)
    

    return wrapper_func