from django.shortcuts import render, get_object_or_404
from .models import Jewelry


# Create your views here.
def all_jewelries(request):
    """ to render all jewelries, as well as sorting and searching functions  """

    jewelries = Jewelry.objects.all()

    context = {
        'jewelries': jewelries,
    }

    return render(request, 'jewelries/jewelries.html', context)


def jewelry_detail(request, jewelry_id):
    """ to render each jewelry with details  """

    jewelry = get_object_or_404(Jewelry, pk=jewelry_id)

    context = {
        'jewelry': jewelry,
    }

    return render(request, 'jewelries/jewelry_detail.html', context)
