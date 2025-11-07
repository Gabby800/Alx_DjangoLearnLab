from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library
from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"   
    context_object_name = "library"


# Function-Based View
def book_list(request):
    books = Book.objects.all()

    output = ""
    for book in books:
        output += f"{book.title} - {book.author.name}\n"

    return HttpResponse(output, content_type="text/plain")

class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"
