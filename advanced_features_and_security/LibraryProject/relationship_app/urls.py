from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from .views import admin_view, librarian_view, member_view, register
from . import views
from .views import add_book, edit_book, delete_book

urlpatterns = [
    path('books/', list_books, name='list_books'),   
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('register/', register, name='register'),
    path('login/',LoginView.as_view(template_name="relationship_app/login.html"), name='login'),
    path( 'logout/',LogoutView.as_view(template_name="relationship_app/logout.html" ), name='logout'),
    path("roles/admin/", admin_view, name="admin_view"),
    path("roles/librarian/", librarian_view, name="librarian_view"),
    path("roles/member/", member_view, name="member_view"),
     path("add_book/", add_book, name="add_book"),
    path("edit_book/<int:book_id>/edit/", edit_book, name="edit_book"),
    path("delete_book/<int:book_id>/delete/", delete_book, name="delete_book"),
]



