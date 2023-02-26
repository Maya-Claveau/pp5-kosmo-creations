from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from jewelries.models import Jewelry
from profiles.models import UserProfile
from .models import Wishlist


@login_required
def wishlist(request):
    """ display the wishlist page """

    template = 'wishlist/wishlist.html'
    context = {
        'on_page': True,
    }
    return render(request, template, context)


@login_required
def add_to_wishlist(request, jewelry_id):
    """ add a jewelry to the wishlist"""
    user = UserProfile.objects.get(user=request.user)
    jewelry = get_object_or_404(Jewelry, pk=jewelry_id)
    wishlist_exists = Wishlist.objects.filter(
        user=user, jewelry=jewelry
        ).exists()

    if wishlist_exists:
        wishlist_item = Wishlist.objects.get(
            user=user,
            jewelry=jewelry
        )
        wishlist_item.delete()
        messages.info(request, f'{wishlist_item} already in your wishlist!')
        return redirect(reverse('jewelry_detail', args=[jewelry.id]))
    else:
        wishlist_item = Wishlist.objects.create(
            user=user,
            jewelry=jewelry
        )
        messages.success(
            request, f'Successfully added {wishlist_item} to your wishlist!')
        return redirect(reverse('jewelry_detail', args=[jewelry.id]))


@login_required
def remove_from_wishlist(request, jewelry_id):
    """ remove from the wishlist"""
    user = UserProfile.objects.get(user=request.user)
    jewelry = get_object_or_404(Jewelry, pk=jewelry_id)
    wishlist_item = Wishlist.objects.get(user=user, jewelry=jewelry)
    wishlist_item.delete()
    messages.success(request, f'Successfully removed {jewelry.name}')
    return redirect(reverse('wishlist'))
