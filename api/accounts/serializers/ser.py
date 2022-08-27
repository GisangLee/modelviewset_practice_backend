from rest_framework import serializers
from accounts import models as account_models

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,)

    def already_exists(self, username):

        try:

            already_exists = account_models.User.objects.get(username = username)
            if already_exists:
                return True

        except account_models.User.DoesNotExist:
            return False

    def create(self, validated_data):
        user_exists = self.already_exists(validated_data["username"])

        if user_exists:
            return False
        
        new_user = account_models.User.objects.create(username=validated_data["username"], email=validated_data["password"])

        new_user.set_password(validated_data["password"])

        new_user.gender = validated_data["gender"]
        new_user.age = validated_data["age"]
        new_user.phone_number = validated_data["phone_number"]

        new_user.save()

        return new_user
        

    class Meta:
        model = account_models.User
        fields = ("username", "email", "password", "gender", "age", "phone_number",)