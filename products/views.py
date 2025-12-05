from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower 
from .models import Product, Category, Watchlist
from django.contrib.auth.decorators import login_required

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'    

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(size__icontains=query) | Q(price__icontains=query) 
            products = products.filter(queries)
    current_sorting = f'{sort}_{direction}'
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    images = product.images.all()
    images_count = product.images.count()
    user_watched_products = []
    if request.user.is_authenticated:
        user_watched_products = request.user.watchlist.values_list('product_id', flat=True)

    context = {
        'product': product,
        'images': images,
        'images_count': images_count,
        'user_watched_products': list(user_watched_products),
    }
    return render(request, 'products/product_detail.html', context)


@login_required
def watchlist_view(request):
    watchlist_items = request.user.watchlist.select_related('product')
    return render(request, 'products/watchlist.html', {'watchlist_items': watchlist_items})


@login_required
def add_to_watchlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    watchlist_item, created = Watchlist.objects.get_or_create(user=request.user, product=product)
    if created:
        messages.success(request, 'Product added to your watchlist.')
    else:
        messages.info(request, 'Product is already in your watchlist.')
    return redirect('product_detail', product_id=product.id)


@login_required
def remove_from_watchlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Watchlist.objects.filter(user=request.user, product=product).delete()
    messages.success(request, 'Product removed from your watchlist.')
    return redirect('watchlist') 
