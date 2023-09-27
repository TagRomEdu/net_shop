from django.urls import path

from catalog.models import Product
from catalog.views import home, contacts, product


urlpatterns = [
    path('', home),
    path('contacts/', contacts),
    path('product/<int:id>/', product)
]
