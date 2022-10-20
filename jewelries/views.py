from django.shortcuts import render
from .models import Product


# Create your views here.
def all_jewelries(request):
    """ to render all jewelries, as well as sorting and searching functions  """

    jewelries = Product.objects.all()

    context = {
        'jewelries': jewelries,
    }

    return render(request, 'jewelries/jewelries.html', context)
