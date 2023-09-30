from django.urls import path


from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view()),
    path('contacts/', contacts),
    path('product/<int:pk>/', ProductDetailView.as_view())
]
