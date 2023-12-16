from django.urls import re_path

from . import views

urlpatterns = [
    re_path('api/books/(?P<pk>[0-9]*)', views.books, name='books'),
]