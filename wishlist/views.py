from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from jewelries.models import Jewelry
from profiles.models import UserProfile
from .models import WishlistItem


@login_required
def wishlist(request):
    """ display the wishlist page """
    if request.method == 'POST':
        jewelry_name = request.POST.get('jewelry.jewelry_name')
        jewelry_description = request.POST.get('jewelry.jewelry_description')
        jewelry_url = request.POST.get('jewelry_url')
        WishlistItem.objects.create(
            user=request.user,
            jewelry_name=Jewelry.jewelry_name,
            jewelry_description=Jewelry.jewelry_description,
            jewelry_url=Jewelry.jewelry_url
            )
        return redirect('wishlist')

    items = WishlistItem.objects.filter(user=request.user)
    template = 'wishlist/wishlist.html'
    return render(request, template, {'items': items})


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
        return redirect(reverse('jewelry_detail', args=[jewelry.id]))
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
