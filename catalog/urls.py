from django.urls import path


from catalog.apps import CatalogConfig
from catalog.views import (contacts, ProductListView, ProductDetailView,
                           BlogListView, BlogDetailView, BlogCreateView, BlogDeleteView, BlogUpdateView)

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view()),
    path('contacts/', contacts),
    path('product/<int:pk>/', ProductDetailView.as_view()),
    path('blog_list/', BlogListView.as_view(), name='list'),
    path('blog_list/form/', BlogCreateView.as_view(), name='create'),
    path('blog_list/update/<slug>/', BlogUpdateView.as_view(), name='update'),
    path('blog_list/confirm_delete/<slug>/', BlogDeleteView.as_view(), name='delete'),
    path('blog_list/<slug>/', BlogDetailView.as_view(), name='detail'),
]
