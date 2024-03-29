from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from jewelries.models import Jewelry


# Create your views here.
def view_shopping_cart(request):
    """ a view to render the shopping cart page """

    return render(request, 'shopping_cart/shopping_cart.html')


def add_to_cart(request, item_id):
    """ add quantity of the specified product in the shopping cart """

    jewelry = get_object_or_404(Jewelry, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shopping_cart = request.session.get('shopping_cart', {})

    if item_id in list(shopping_cart.keys()):
        shopping_cart[item_id] += quantity
        messages.success(
            request,
            f'Updated {jewelry.name} quantity to {shopping_cart[item_id]}'
            )

    else:
        shopping_cart[item_id] = quantity
        messages.success(
            request,
            f'Added {jewelry.name} to your shopping cart'
            )

    request.session['shopping_cart'] = shopping_cart
    return redirect(redirect_url)


def modify_cart(request, item_id):
    """
    modify the quantity of the specified product in the shopping cart
    """

    jewelry = get_object_or_404(Jewelry, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    shopping_cart = request.session.get('shopping_cart', {})

    if quantity > 0:
        shopping_cart[item_id] = quantity
        messages.success(
            request,
            f'Updated {jewelry.name} quantity to {shopping_cart[item_id]}'
            )
    else:
        shopping_cart.pop(item_id)
        messages.success(
            request,
            f'Removed {jewelry.name} from you shopping cart'
            )

    request.session['shopping_cart'] = shopping_cart
    return redirect(reverse('view_shopping_cart'))


def delete_from_cart(request, item_id):
    """ delete item from shopping cart """

    try:
        jewelry = get_object_or_404(Jewelry, pk=item_id)
        shopping_cart = request.session.get('shopping_cart', {})

        shopping_cart.pop(item_id)
        messages.success(
            request,
            f'Deleted {jewelry.name} from your shopping cart'
            )

        request.session['shopping_cart'] = shopping_cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error deleting item: {e}')
        return HttpResponse(status=500)
