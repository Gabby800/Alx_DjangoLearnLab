from rest_framework import generics
from .serializers import BookSeriaizer
from .models import Book


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSeriaizer
    
