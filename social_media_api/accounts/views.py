from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import CustomUser
from rest_framework import status, permissions
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer, UserFollowSerializer


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "message": "Registration successful",
            "token": token.key,
            "user": UserSerializer(user).data
        }, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "message": "Login successful",
            "token": token.key,
            "user": UserSerializer(user).data
        })
        

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response(UserSerializer(user).data)

    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message": "Profile updated",
            "user": serializer.data
        })

# Follow a user
class FollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserFollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        user_to_follow = get_object_or_404(CustomUser, pk=pk)

        if request.user == user_to_follow:
            return Response(
                {"detail": "You cannot follow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )

        request.user.following.add(user_to_follow)
        return Response(
            {"detail": f"You are now following {user_to_follow.username}."},
            status=status.HTTP_200_OK
        )


class UnfollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        user_to_unfollow = get_object_or_404(CustomUser, pk=pk)

        request.user.following.remove(user_to_unfollow)
        return Response(
            {"detail": f"You have unfollowed {user_to_unfollow.username}."},
            status=status.HTTP_200_OK
        )
