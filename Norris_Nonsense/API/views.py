from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from Norris_Nonsense.API.serializers import (
    JokeTextSerializer,
    JokeSerializer,
    CustomTokenObtainPairSerializer,
    CustomUserSerializer,
)
from Norris_Nonsense.models import Joke, CustomUser


class CreateUserAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]


class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(
            username=username,
            password=password
        )

        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                return Response({
                    'token': login_serializer.validated_data.get('access'),
                    'refresh-token': login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'message': 'Inicio de sesión exitoso',
                }, status=status.HTTP_200_OK)
            return Response({'error': 'Nombre de usuario o contraseña incorrectos'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Nombre de usuario o contraseña incorrectos'}, status=status.HTTP_400_BAD_REQUEST)


class Logout(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        user = CustomUser.objects.filter(id=request.data.get('user', 0))
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message': 'Sesión cerrada exitosamente'}, status=status.HTTP_200_OK)
        return Response({'error': 'No se pudo cerrar la sesión'}, status=status.HTTP_400_BAD_REQUEST)


class GetJokeAPIView(APIView):
    serializer_class = JokeTextSerializer

    def get(self, request):
        serializer = JokeTextSerializer()
        joke_text = serializer.get_joke()
        data = {'joke': joke_text}
        return Response(data, status=status.HTTP_200_OK)


class MyJokesCreateAPIView(generics.CreateAPIView):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer


class MyJokesListAPIView(generics.ListAPIView):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer


class MyJokesUpdateAPIView(generics.UpdateAPIView):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer


class MyJokesDeleteAPIView(generics.DestroyAPIView):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer


