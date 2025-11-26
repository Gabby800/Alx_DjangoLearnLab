from django.db import models

# Author Model
# ---------------------------------------------------------
# This model represents an author in the system.
# It currently stores only the author's name, but can be
# extended later (e.g., biography, nationality, etc.).
# An Author can have many Books (one-to-many relationship).
# ---------------------------------------------------------
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

# BookSerializer
# ---------------------------------------------------------
# Serializes all fields of the Book model.
# Includes custom validation to ensure the publication year
# is not in the future.
# ---------------------------------------------------------
class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title