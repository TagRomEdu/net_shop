from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Product, Blog


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


def contacts(request):
    return render(request, 'catalog/contacts.html')


class BlogCreateView(CreateView):
    model = Blog


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog


class BlogUpdateView(UpdateView):
    model = Blog


class BlogDeleteView(DeleteView):
    model = Blog
