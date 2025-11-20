from rest_framework import serializers
from .models import Book

class BookSeriaizer(serializers.Serializer):
    class meta:
        model = Book
        fields = ['id, title, author']
