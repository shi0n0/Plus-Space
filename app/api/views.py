from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login, logout, authenticate
from api.serializer import CustomUserSerializer
from django.contrib.auth.decorators import login_required

# ユーザー登録APIビュー
@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ユーザーログインAPIビュー
@api_view(['POST'])
def login_user(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return Response({'message': 'ログインに成功しました。'}, status=status.HTTP_200_OK)
        return Response({'message': '無効なログイン情報です。'}, status=status.HTTP_401_UNAUTHORIZED)

# ユーザーログアウトAPIビュー
@login_required
@api_view(['POST'])
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return Response({'message': 'ログアウトしました。'}, status=status.HTTP_200_OK)