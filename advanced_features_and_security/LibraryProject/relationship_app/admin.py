from django.contrib import admin
from .models import Author, Book, Library, Librarian, UserProfile
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "role")
    list_filter = ("role",)
    search_fields = ("user__username", "user__email")

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "date_of_birth", "is_staff", "is_superuser")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("date_of_birth", "profile_photo")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "date_of_birth", "profile_photo", "is_staff", "is_superuser")
        }),
    )

    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
