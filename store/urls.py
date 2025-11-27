from django.urls import path
from .views import (
    ProductListCreateView, ProductDetailView,
    CategoryListCreateView, CategoryDetailView
)

#API Endpoints

app_name = "store"

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]
