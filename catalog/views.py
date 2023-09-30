from django.shortcuts import render
from django.views.generic import ListView

from catalog.models import Product


'''def contacts(request):
    return render(request, 'catalog/contacts.html')


def product(request, id):
    context = {
        'page_id': id,
        'object': Product.objects.get(id=id)
               }
    return render(request, 'catalog/product.html', context)'''


class ProductListView(ListView):
    model = Product


def contacts(request):
    return render(request, 'catalog/contacts.html')


def product(request, id):
    context = {
        'page_id': id,
        'object': Product.objects.get(id=id)
               }
    return render(request, 'catalog/product.html', context)