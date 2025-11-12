from django.contrib import admin
from .models import Author, Book, Library, Librarian, UserProfile
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "role")
    list_filter = ("role",)
    search_fields = ("user__username", "user__email")

