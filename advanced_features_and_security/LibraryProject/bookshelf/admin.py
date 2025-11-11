from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import CustomUserAdmin
from .models import CustomUser

# Custom admin configuration for the Book model
admin.site.register(CustomUser, CustomUserAdmin)