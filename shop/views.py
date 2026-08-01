from django.shortcuts import get_object_or_404, render

from .models import Product


def home(request):
    products = Product.objects.filter(is_active=True)[:8]
    return render(request, 'shop/index.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, 'shop/product_detail.html', {'product': product})
