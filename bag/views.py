from django.shortcuts import render, redirect, reverse

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

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
    bag = request.session.get('bag', {})


    bag.pop(str(item_id), None)

    request.session['bag'] = bag
    return redirect('view_bag')
