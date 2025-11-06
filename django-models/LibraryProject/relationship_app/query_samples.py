from relationship_app.models import Author, Book, Library, Librarian

def run_queries():

    # 1. Query all books by a specific author
    author_name = "John Smith"
    try:
        author = Author.objects.get(name=author_name)
        books_by_author = Book.objects.filter(author=author)
        print("Books by", author_name)
        for book in books_by_author:
            print("-", book.title)
    except Author.DoesNotExist:
        print("Author not found")

    # 2. List all books in a library
    library_name = "Central Library"
    try:
        library = Library.objects.get(name=library_name)
        print("\nBooks in", library_name)
        for book in library.books.all():
            print("-", book.title)
    except Library.DoesNotExist:
        print("Library not found")

    # 3. Retrieve the librarian for a library
    try:
        librarian = Librarian.objects.get(library=library)
        print("\nLibrarian of", library_name + ":", librarian.name)
    except Librarian.DoesNotExist:
        print("Librarian not found")


# Run the function when executed directly
if __name__ == "__main__":
    run_queries()
