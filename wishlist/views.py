from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from jewelries.models import Jewelry
from profiles.models import UserProfile
from .models import WishlistItem


@login_required
def wishlist_view(request):
    """ display the wishlist page """
    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = WishlistItem.objects.filter(user=user)
    template = 'wishlist/wishlist.html'
    context = {
        'wishlist': wishlist,
    }

    return render(request, template, context)


@login_required
def add_to_wishlist(request, jewelry_id):
    """ add a jewelry to the wishlist"""
    user = get_object_or_404(UserProfile, user=request.user)
    jewelry = get_object_or_404(Jewelry, pk=jewelry_id)

    WishlistItem.objects.create(
        user=user,
        jewelry=jewelry
    )
    messages.success(
        request, f'{jewelry.name} has been added to your Wishlist!')

    return redirect(reverse('jewelry_detail', args=[jewelry.id]))


@login_required
def remove_from_wishlist(request, item_id):
    """ remove jewelry from the wishlist"""
    user = get_object_or_404(UserProfile, user=request.user)
    # get the item from the wishlist to be removed
    item = get_object_or_404(Jewelry, pk=item_id)
    # check if the reuquested user owns the item to be removed
    WishlistItem.objects.filter(user=user, jewelry=item).delete()
    messages.success(
            request,
            f'Successfully removed {item.name} from your wishlist!'
            )
    return redirect(reverse('jewelry_detail', args=[item.id]))
