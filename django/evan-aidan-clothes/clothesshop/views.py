from django.shortcuts import render, get_object_or_404 # Import get_object_or_404
from django.http import HttpResponse
from .models import Listing

# Create your views here.


def index(request):
    listings = Listing.objects.all()
    context = {"listings": listings}
    return render(request, "clothesshop/index.html", context)

def listing(request, listing_id):
    # This will fetch the listing or return a 404 Not Found page if it doesn't exist.
    listing_obj = get_object_or_404(Listing, pk=listing_id)

    # Prepare the context dictionary to pass the listing object to the template
    context = {
        "listing": listing_obj,
        "shit": "hell yeah"
    }

    # Render the new detail template with the context
    return render(request, "clothesshop/listing_detail.html", context)

