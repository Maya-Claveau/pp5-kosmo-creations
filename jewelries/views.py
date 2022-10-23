from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Jewelry, Category


# Create your views here.
def all_jewelries(request):
    """ to render all jewelries, as well as sorting and searching functions  """

    jewelries = Jewelry.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            jewelries = jewelries.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                jewelries = jewelries.annotate(lower_name=lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            jewelries = jewelries.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criterial!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            jewelries = jewelries.filter(queries)

    requested_sorting = f'{sort}_{direction}'

    context = {
        'jewelries': jewelries,
        'search_term': query,
        'requested_categories': categories,
        'requested_sorting': requested_sorting,
    }

    return render(request, 'jewelries/jewelries.html', context)


def jewelry_detail(request, jewelry_id):
    """ to render each jewelry with details  """

    jewelry = get_object_or_404(Jewelry, pk=jewelry_id)

    context = {
        'jewelry': jewelry,
    }

    return render(request, 'jewelries/jewelry_detail.html', context)
