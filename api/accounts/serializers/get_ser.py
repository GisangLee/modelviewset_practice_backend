from rest_framework import serializers
from accounts import models as account_models

class UserViewSetSerializer(serializers.ModelSerializer):

    class Meta:

        model = account_models.User
        fields = ("pk", "username", "email", "gender", "phone_number", "age", "is_deleted", "is_superuser", "created_at", "updated_at",)