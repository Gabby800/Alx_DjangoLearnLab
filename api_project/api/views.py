from rest_framework import generics, viewsets
from .serializers import BookSerializer
from .models import Book
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# ============================================
# BookViewSet: Full CRUD API for Book Model
# ============================================
# Authentication:
#   - TokenAuthentication is used.
#   - Users must provide a valid token in the HTTP header:
#       Authorization: Token <user_token>
# 
# Permissions:
#   - IsAuthenticated ensures only logged-in users can access any CRUD operations.
#   - Unauthenticated requests will get HTTP 401 Unauthorized.
# 
# Functionality:
#   - list: GET /books/       → List all books
#   - retrieve: GET /books/<id>/ → Get a single book
#   - create: POST /books/    → Create a new book
#   - update: PUT /books/<id>/ → Update a book
#   - partial_update: PATCH /books/<id>/ → Partial update
#   - destroy: DELETE /books/<id>/ → Delete a book
#
# ============================================
# BookListView: Manual GET and POST API for Books
# ============================================
# Authentication:
#   - TokenAuthentication is used here as well.
#   - Requests must include a valid token.
# 
# Permissions:
#   - IsAuthenticated ensures only authenticated users can list or create books.
# 
# GET Method:
#   - Returns a list of all Book objects in JSON format.
# POST Method:
#   - Accepts JSON data to create a new Book object.
#   - Validates data before saving; returns errors if invalid.

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
       books = Book.objects.all()
       serializer = BookSerializer (books, many=True)
       return Response(serializer.data)
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


        
    



