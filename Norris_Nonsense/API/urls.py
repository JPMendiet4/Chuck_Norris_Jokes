from django.urls import path
from Norris_Nonsense.API.views import (
    GetJokeAPIView, MyJokesCreateAPIView, MyJokesListAPIView,
    MyJokesUpdateAPIView, MyJokesDeleteAPIView,
    Login, Logout, CreateUserAPIView,
)

urlpatterns = [
    path('users/create/', CreateUserAPIView.as_view(), name='Create User'),
    path('login/', Login.as_view(), name='Login'),
    path('logout/', Logout.as_view(), name='Logout'),
    path('jokes/random/', GetJokeAPIView.as_view(), name='Get Jokes'),
    path('jokes/', MyJokesCreateAPIView.as_view(), name='Favorites Jokes'),
    path('jokes/list/', MyJokesListAPIView.as_view(), name='My Jokes'),
    path('jokes/update/<int:pk>/', MyJokesUpdateAPIView.as_view(), name='Update Joke'),
    path('jokes/delete/<int:pk>/', MyJokesDeleteAPIView.as_view(), name='Delete Joke'),
]
