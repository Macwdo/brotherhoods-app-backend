import http
from rest_framework import status
from rest_framework.request import Request
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from project.types.auth import LoginRequest


class MeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email']

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

@permission_classes([IsAuthenticated])
def me(self, request):
    serializer = MeUserSerializer(request.user)
    serializer.is_valid()
    return Response(serializer.data)


def validated_request_data(request: dict[str, str]) -> LoginRequest:
    try:
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

    except serializers.ValidationError as e:
        raise Response(
            {'error': e},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    return LoginRequest(
        username=serializer.validated_data.get("username"),
        password=serializer.validated_data.get("password"),
    )

def validated_user(username: str, password: str) -> User | None:
    user = User.objects.filter(username=username).first()
    if user is None:
        raise Response(
            {'error': 'User not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    
    if not user.check_password(password):
        raise Response(
            {'error': 'Invalid password'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    return user

@api_view(http_method_names=['POST'])
def user_by_credentials(request: Request):
    request_data = validated_request_data(request)
    user = validated_user(request_data.username, request_data.password)
    serializer = MeUserSerializer(instance=user)

    return Response(data=serializer.data, status=status.HTTP_200_OK)