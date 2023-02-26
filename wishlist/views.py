from django.shortcuts import render


# Create your views here.
def view_wishlist(request):
    """ a view to render the wishlist page """

    return render(request, 'wishlist/wishlist.html')
