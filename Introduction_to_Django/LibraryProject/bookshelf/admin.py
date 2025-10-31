from django.contrib import admin
from .models import Book

# Custom admin configuration for the Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to display
    search_fields = ('title', 'author')                     # Search bar fields
    list_filter = ('publication_year',)                     # Sidebar filter
