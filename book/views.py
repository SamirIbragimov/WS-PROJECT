from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.views.generic.edit import CreateView, DeleteView, UpdateView


class BookListView(ListView):
    model = Book
    template_name = "book_list.html"
    context_object_name = "books"


class BookDetailViews(DetailView):
    model = Book
    template_name = "book_detail.html"
    context_object_name = "book"


class BookCreateViews(CreateView):
    model = Book
    fields = '__all__'
    template_name = "book_create.html"
    success_url = reverse_lazy("book-list")


class BookDeleteViews(DeleteView):
    model = Book
    template_name = "book_delete.html"
    success_url = reverse_lazy("book-list")


class BookUpdateViews(UpdateView):
    model = Book
    template_name = "book_update.html"
    fields = '__all__'
    success_url = reverse_lazy("book-list")
