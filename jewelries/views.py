from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Jewelry


# Create your views here.
def all_jewelries(request):
    """ to render all jewelries, as well as sorting and searching functions  """

    jewelries = Jewelry.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criterial!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            jewelries = jewelries.filter(queries)

    context = {
        'jewelries': jewelries,
        'search_term': query,
    }

    return render(request, 'jewelries/jewelries.html', context)


def jewelry_detail(request, jewelry_id):
    """ to render each jewelry with details  """

    jewelry = get_object_or_404(Jewelry, pk=jewelry_id)

    context = {
        'jewelry': jewelry,
    }

    return render(request, 'jewelries/jewelry_detail.html', context)
