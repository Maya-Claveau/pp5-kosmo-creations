from django.shortcuts import render


# Create your views here.
def view_shopping_cart(request):
    """ a view to render the shopping cart page """

    return render(request, 'shopping_cart/shopping_cart.html')
