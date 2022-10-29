from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_shopping_cart, name='view_shopping_cart'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
    path('modify/<item_id>/', views.modify_cart, name='modify_cart'),
    path('delete/<item_id>/', views.delete_from_cart, name='delete_from_cart'),
]
