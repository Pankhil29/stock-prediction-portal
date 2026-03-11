from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,min_length=8, style={"input_type":"password"})
    class Meta:
        model = User
        fields = ["username","email","password"]
    # User.objects.create = save the password in a plain Text
    # User.objects.create_user = save the password in a hased format
    def create(self,validated_data):
        # user = User.objects.create_user(
        #     validated_data["username"],
        #     validated_data["email"],
        #     validated_data["password"]
        # )
        user = User.objects.create_user(**validated_data)
        return user
