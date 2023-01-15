from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_jewelries, name='jewelries'),
    path('<int:jewelry_id>/', views.jewelry_detail, name='jewelry_detail'),
    path('add/', views.add_jewelry, name='add_jewelry'),
    path('edit/<int:jewelry_id>/', views.edit_jewelry, name='edit_jewelry'),
    path('delete/<int:jewelry_id>/', views.delete_jewelry, name='delete_jewelry'),  # noqa
]
