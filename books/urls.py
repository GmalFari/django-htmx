from django.urls import path 
from .views import (
    create_book,
    create_book_form,
    detail_book,
    delete_book,
    update_book,
)
urlpatterns = [
    path("htmx/book-form",create_book_form,name="book-form"),
    path("htmx/book/<pk>",detail_book ,name="book-detail"),
    path("htmx/book/<pk>/update/",update_book ,name="book-update"),
    path("htmx/book/<pk>/delete/",delete_book ,name="book-delete"),
    path("<pk>/",create_book,name="create-book"),
]
