from django.shortcuts import render, redirect
from django.contrib import messages

from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    product = Product.objects.get(pk=item_id)


    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Increased {product.name} quantity to your bag')

    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')


    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified product to the specified amount """

    current_quantity = int(request.POST.get('quantity', 0))
    bag = request.session.get('bag', {})


        # Enforce min/max limits
    new_quantity = max(1, min(99,  current_quantity))

    if new_quantity > 0:
        bag[item_id] = new_quantity
    else:
        bag.pop(item_id, None)

    request.session['bag'] = bag
    return redirect('view_bag')
  

def remove_from_bag(request, item_id):
    """ Remove the item from the shopping bag """
    product = Product.objects.get(pk=item_id)
    bag = request.session.get('bag', {})


    bag.pop(str(item_id), None)

    messages.success(request, f'Deleted {product.name} from your bag')

    request.session['bag'] = bag
    return redirect('view_bag')
