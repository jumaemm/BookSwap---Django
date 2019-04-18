from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import (ListView, DetailView, CreateView)
from .models import Book
from .forms import BookForm
from django.utils import timezone
# Create your views here.
class BookListView(ListView):
    model = Book

    def get_queryset(self):
        return Book.objects.filter(posted_date__lte = timezone.now()).order_by('posted_date')

class BookDetailView(DetailView):
    model = Book

class CreateBookView(CreateView):
    form_class = BookForm
    model = Book


def book_post(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.post_book()
    return redirect('book_detail', pk=pk)
