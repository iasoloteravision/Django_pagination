from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Item

def item_list(request):
    # Retrieve the page number from the query string
    page_number = request.GET.get('page', 1)

    # Number of items to show per page
    items_per_page = 5

    # Query all items
    items = Item.objects.all()

    # Paginate the items
    paginator = Paginator(items, items_per_page)
    page_obj = paginator.get_page(page_number)

    return render(request, 'item_list.html', {'page_obj': page_obj})