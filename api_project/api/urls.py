from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'book', BookViewSet, basename='Book')

urlpatterns = [path('', include(router.urls)),
               path('book/', BookList.as_view(), name='book-list')
               ]



