from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from Norris_Nonsense.models import CustomUser, Joke
import requests


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

    def to_representation(self, instance):
        return {
                "password": instance.password,
                "is_superuser": instance.is_superuser,
                "username": instance.username,
                "first_name": instance.first_name,
                "last_name": instance.last_name,
                "email": instance.email,
                "is_staff": instance.is_staff,
                "is_active": instance.is_active,
                "name": instance.name
        }


class JokeTextSerializer(serializers.Serializer):
    def get_joke(self):
        url = "https://api.chucknorris.io/jokes/random"
        response = requests.get(url)
        if response.status_code == 200:
            joke_text = response.json()['value']
            return joke_text
        raise serializers.ValidationError(
            {'error': 'No fue posible conectarse a la API de Chuck Norris'}
        )


class JokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joke
        fields = '__all__'

    def create(self, validated_data):
        favorites = validated_data.get('favorites')
        if favorites:
            joke = Joke.objects.create(**validated_data)
            return joke
        else:
            raise serializers.ValidationError("Solo se pueden agregar chistes favoritos")





