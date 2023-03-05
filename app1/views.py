from django.shortcuts import render
from .models import Author, Book
from django.views.generic.list import ListView

# Create your views here.

class BookListView(ListView):
    model = Book
    template_name="app1/books.html"

