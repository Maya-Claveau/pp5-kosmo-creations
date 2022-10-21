from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_jewelries, name='jewelries'),
    path('<jewelry_id>', views.jewelry_detail, name='jewelry_detail')
]
