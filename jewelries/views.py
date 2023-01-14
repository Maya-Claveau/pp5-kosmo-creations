from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Jewelry, Category
from .forms import JewelryForm


# Create your views here.
def all_jewelries(request):
    """ to render all jewelries, as well as sorting and searching functions """

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
                jewelries = jewelries.annotate(lower_name=Lower('name'))
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
                messages.error(
                    request, "You didn't enter any search criterial!"
                    )
                return redirect(reverse('jewelries'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)  # noqa
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


def add_jewelry(request):
    """ add a jewelry to the e-shop """
    # if not request.user.is_superuser:
    #     messages.error(request, 'Sorry, only store owners can do that.')
    #     return redirect(reverse('home'))

    # if request.method == 'POST':
    #     form = JewelryForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         jewelry = form.save()
    #         messages.success(request, 'Jewelry Added Successfully!')
    #         return redirect(reverse('jewelry_detail', args=[jewelry.id]))
    #     else:
    #         messages.error(request, 'Failed to add product. Please try again.')
    # else:
    #     form = JewelryForm()

    form = JewelryForm()
    template = 'jewelries/add_jewelry.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
