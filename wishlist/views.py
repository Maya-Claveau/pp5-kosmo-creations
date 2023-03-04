from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from jewelries.models import Jewelry
from profiles.models import UserProfile
from .models import WishlistItem


@login_required
class wishlistView(generic.View):
    """ display the wishlist page """
    def get(self, *args, **kwargs):
        wish_items = WishlistItem.objects.filter(user=self.request.user)
        context = {
            'wish_items': wish_items
        }
        return render(self.request, 'wishlist/wishlist.html', context)


@login_required
def add_to_wishlist(request, jewelry_id):
    """ add a jewelry to the wishlist"""
    user = UserProfile.objects.get(user=request.user)
    jewelry = get_object_or_404(Jewelry, id=jewelry_id)
    wishlist_exists = WishlistItem.objects.filter(
        user=user, jewelry=jewelry
        ).exists()

    if wishlist_exists:
        wishlist_item = WishlistItem.objects.get(
            user=user,
            jewelry=jewelry
        )
        wishlist_item.delete()
        messages.info(request, f'{wishlist_item} already in your wishlist!')
        return redirect('wishlist')
    else:
        wishlist_item = WishlistItem.objects.create(
            user=user,
            jewelry=jewelry
        )
        messages.success(
            request, f'Successfully added {wishlist_item} to your wishlist!')
        return redirect('wishlist')


@login_required
def remove_from_wishlist(request, jewelry_id):
    """ remove from the wishlist"""
    item = WishlistItem.objects.get(id=jewelry_id)
    if item.user == request.user:
        item.delete()
        messages.success(request, f'Successfully removed {jewelry.name}')
    return redirect('wishlist')
