from django.shortcuts import render, get_object_or_404
from .models import Product, Image

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    images = product.images.all()
    images_count = product.images.count()

    context = {
        'product': product,
        'images': images,
        'images_count': images_count,

    }

    return render(request, 'products/product_detail.html', context)