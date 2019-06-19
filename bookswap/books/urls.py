from django.urls import path
from . import views

urlpatterns = [
    path("", views.BookListView.as_view(), name = "book_list"),
    path("books/<int:pk>/", views.BookDetailView.as_view(), name = "book_detail"),
    path("books/create_book/", views.CreateBookView.as_view(), name = "create_book")
]
