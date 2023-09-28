from django.shortcuts import render

from catalog.models import Product


def home(request):
    context = {
        'object_list': Product.objects.all()
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    return render(request, 'catalog/contacts.html')


def product(request, id):
    context = {
        'page_id': id,
        'object': Product.objects.get(id=id)
               }
    return render(request, 'catalog/product.html', context)
