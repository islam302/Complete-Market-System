from django.contrib import admin
from .models import UserModel
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(UserModel)
class UserAdmin(BaseUserAdmin):
    pass
