# CRUD Operations for Book Model

---

## Create Operation

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Output: <Book: 1984 by George Orwell (1949)>


Book.objects.all()
# Output: <QuerySet [<Book: 1984 by George Orwell (1949)>]>

book.title = "Nineteen Eighty-Four"
book.save()
Book.objects.get(id=book.id)
# Output: <Book: Nineteen Eighty-Four by George Orwell (1949)>

book.delete()
Book.objects.all()
# Output: <QuerySet []>
