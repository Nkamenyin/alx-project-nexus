from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<slug:slug>/', views.category_products, name='category_products'),
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),
]
