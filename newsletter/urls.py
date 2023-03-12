from django.urls import path
from . import views


urlpatterns = [
    path('', views.newsletter_view, name='newsletter'),
]
