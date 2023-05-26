from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


class CustomUser(AbstractUser):
    name = models.CharField(max_length=100, blank=True, null=True)


class Joke(models.Model):
    joke = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="jokes")
    favorites = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.joke} - {self.user.username}"
