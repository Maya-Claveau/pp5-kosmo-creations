from django.urls import path
from . import views


urlpatterns = [
    path('', views.wishlist_view, name='wishlist'),
    path(
        'add_to_wishlist/<int:jewelry_id>/',
        views.add_to_wishlist,
        name="add_to_wishlist"
    ),
    path(
        'remove_from_wishlist/<int:item_id>/',
        views.remove_from_wishlist,
        name="remove_from_wishlist"
    ),
]
