from django.test import TestCase

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Book, Author

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create user
        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )

        # Create author
        self.author = Author.objects.create(name="John Doe")

        # Create books
        self.book1 = Book.objects.create(
            title="Alpha Book",
            publication_year=2020,
            author=self.author
        )
        self.book2 = Book.objects.create(
            title="Beta Book",
            publication_year=2023,
            author=self.author
        )

        # Authenticated client
        self.client = APIClient()
        self.client.login(username="testuser", password="password123")

    # -----------------------------------------------------------
    # LIST VIEW TESTS
    # -----------------------------------------------------------
    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # -----------------------------------------------------------
    # DETAIL VIEW TEST
    # -----------------------------------------------------------
    def test_retrieve_book(self):
        url = reverse('book-detail', kwargs={"pk": self.book1.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Alpha Book")

    # -----------------------------------------------------------
    # CREATE VIEW TEST
    # -----------------------------------------------------------
    def test_create_book_authenticated(self):
        url = reverse('book-create')
        data = {
            "title": "New Book",
            "publication_year": 2024,
            "author": self.author.id
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        client = APIClient()
        url = reverse('book-create')
        data = {
            "title": "Unauthorized Book",
            "publication_year": 2024,
            "author": self.author.id
        }
        response = client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # -----------------------------------------------------------
    # UPDATE TEST
    # -----------------------------------------------------------
    def test_update_book(self):
        url = reverse('book-update', kwargs={"pk": self.book1.pk})
        data = {"title": "Updated Alpha Book", "publication_year": 2019, "author": self.author.id}

        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Alpha Book")

    # -----------------------------------------------------------
    # DELETE TEST
    # -----------------------------------------------------------
    def test_delete_book(self):
        url = reverse('book-delete', kwargs={"pk": self.book2.pk})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # -----------------------------------------------------------
    # FILTERING TEST
    # -----------------------------------------------------------
    def test_filter_books_by_publication_year(self):
        url = f"{reverse('book-list')}?publication_year=2020"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Alpha Book")

    # -----------------------------------------------------------
    # SEARCH TEST
    # -----------------------------------------------------------
    def test_search_books(self):
        url = f"{reverse('book-list')}?search=Beta"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Beta Book")

    # -----------------------------------------------------------
    # ORDERING TEST
    # -----------------------------------------------------------
    def test_order_books_by_title(self):
        url = f"{reverse('book-list')}?ordering=title"
        response = self.client.get(url)

        titles = [book["title"] for book in response.data]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(titles, ["Alpha Book", "Beta Book"])

