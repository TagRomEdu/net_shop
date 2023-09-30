from django.urls import path


from catalog.apps import CatalogConfig
from catalog.views import contacts, product, ProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view()),
    path('contacts/', contacts),
    path('product/<int:id>/', product)
]
