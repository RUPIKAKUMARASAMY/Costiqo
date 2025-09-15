# products_app/views.py
from django.shortcuts import render, get_object_or_404
from .models import Product

# List all products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products_app/product_list.html', {'products': products})

# Detail view for one product
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products_app/product_detail.html', {'product': product})
