from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def home(request):
    products = Product.objects.filter(is_active=True)[:10]  # show 10 products on homepage
    return render(request, 'store/home.html', {'products': products})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'store/categories/category_list.html', {'categories': categories})

def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(is_active=True)
    return render(request, 'store/products/product_list.html', {'category': category, 'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/products/product_detail.html', {'product': product})

