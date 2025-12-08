from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import CustomUser

#create user model
class UserSerializer(serializers.ModelSerializer):
    followers_count = serializers.IntegerField(source='followers.count', read_only=True)

    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'email', 'bio',
            'profile_picture', 'followers', 'followers_count'
        ]
        read_only_fields = ['followers']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'token']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )

        # Create token
        token, _ = Token.objects.get_or_create(user=user)

        # Attach token to serializer response
        user.token = token.key
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError("Invalid username or password")

        token, _ = Token.objects.get_or_create(user=user)

        data['user'] = user
        data['token'] = token.key
        return data

