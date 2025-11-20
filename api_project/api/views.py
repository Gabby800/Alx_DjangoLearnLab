from rest_framework import generics
from .models import Book
from .serializers import BookSeriaizer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSeriaizer
    
