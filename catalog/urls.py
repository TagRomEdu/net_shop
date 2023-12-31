from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import (contacts, ProductListView, ProductDetailView,
                           BlogListView, BlogDetailView, BlogCreateView, BlogDeleteView, BlogUpdateView,
                           ProductCreateView, ProductUpdateView, ProductDeleteView)

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='main'),
    path('contacts/', contacts),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('prod_create/', never_cache(ProductCreateView.as_view()), name='prod_create'),
    path('product/<int:pk>/update/', never_cache(ProductUpdateView.as_view()), name='prod_update'),
    path('product/<int:pk>/confirm_delete/', ProductDeleteView.as_view(), name='prod_delete'),
    path('blog_list/', BlogListView.as_view(), name='list'),
    path('blog_list/form/', never_cache(BlogCreateView.as_view()), name='create'),
    path('blog_list/update/<slug>/', never_cache(BlogUpdateView.as_view()), name='update'),
    path('blog_list/confirm_delete/<slug>/', BlogDeleteView.as_view(), name='delete'),
    path('blog_list/<slug>/', BlogDetailView.as_view(), name='detail'),
]
