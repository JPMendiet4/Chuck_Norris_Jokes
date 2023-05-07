from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import (
    CustomUserCreationForm,
    CustomUserChangeForm,
)
from Norris_Nonsense.models import CustomUser, Joke


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "name",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("name",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("name",)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)


class JokeAdmin(admin.ModelAdmin):
    list_display = [
        "joke",
        "user",
        "created_at",
        "updated_at",
    ]


admin.site.register(Joke, JokeAdmin)
