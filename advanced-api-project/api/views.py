from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    #Enabling django-filters
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,  filters.OrderingFilter,]
    filterset_fields = ['title', 'author', 'publication_year']

    #Enabling Search filter
    search_fields = ['title', 'author_name']

    #Enabling Ordering options
    order_fields = ['title', 'publication_year']
    ordering = ['title'] #default order



class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        print("Creating new book:", serializer.validated_data)
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        print("Updating book:", serializer.validated_data)

        publication_year = serializer.validated_data.get("publication_year")
        if publication_year:
            from datetime import datetime
            current_year = datetime.now().year
            if publication_year > current_year:
                raise ValueError("Publication year cannot be in the future.")

        serializer.save()

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]




    