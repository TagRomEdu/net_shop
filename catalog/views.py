from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Product


'''def contacts(request):
    return render(request, 'catalog/contacts.html')'''


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


def contacts(request):
    return render(request, 'catalog/contacts.html')
