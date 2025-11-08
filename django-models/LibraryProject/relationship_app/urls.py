from django.urls import path
from .views import list_books, LibraryDetailView
from . import views

urlpatterns = [
    path('books/', list_books, name='list_books'),   
    path('library/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
]



