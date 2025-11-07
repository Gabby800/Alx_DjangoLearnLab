from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library


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
