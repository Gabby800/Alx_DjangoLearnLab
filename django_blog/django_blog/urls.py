from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
        # Blog authentication and other URLs
    path('', include('blog.urls')),

]
