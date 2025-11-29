from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

# BookSerializer
# ---------------------------------------------------------
# Serializes all fields of the Book model.
# Includes custom validation to ensure the publication year
# is not in the future.
# ---------------------------------------------------------
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
           raise serializers.ValidationError('Publication year cannot be in the future')
        return value    


# AuthorSerializer
# ---------------------------------------------------------
# This serializer converts Author model instances into JSON.
#
# Fields:
# - name: the author's name
# - books: nested list of books written by the author
#
# Relationship Handling:
# The "books" field uses the BookSerializer to serialize the
# related books. DRF automatically retrieves an author's books
# through the `related_name='books'` defined in the Book model.
#
# The `many=True` argument indicates that an author can have
# multiple books (one-to-many).
#
# The `read_only=True` ensures the nested book list is for
# display only — you cannot create books through the Author
# serializer.
# ---------------------------------------------------------
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name', 'books']
