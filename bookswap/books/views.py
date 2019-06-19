from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (ListView, DetailView, CreateView)
from .models import Book
from .forms import BookForm
from django.utils import timezone
from django.contrib import auth
# Create your views here.
class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'
    def get_queryset(self):
        return Book.objects.filter(posted_date__lte = timezone.now()).order_by('posted_date')

class BookDetailView(DetailView):
    model = Book


class CreateBookView(LoginRequiredMixin, CreateView):
    form_class = BookForm
    model = Book
    success_url = "book_list"
    template_name = "book_form.html"

    def form_valid(self, form):
        print("This is the current user:" +  str(self.request.user.id))
        form.instance.owner = auth.get_user(self.request)
        book_post(self.request, pk = form.instance.id)
        return super().form_valid(form)


def book_post(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.post_book()
    return redirect('book_detail', pk=pk)
