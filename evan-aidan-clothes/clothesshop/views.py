from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Listing, Cart, CartItem

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
    }

    # Render the new detail template with the context
    return render(request, "clothesshop/listing_detail.html", context)

def _get_cart(request):
    """Helper function to get or create a cart."""
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        if not request.session.session_key:
            request.session.create()
        session_key = request.session.session_key
        cart, created = Cart.objects.get_or_create(session_key=session_key)
    return cart

def add_to_cart(request, listing_id):
    """View to add a listing to the cart."""
    product = get_object_or_404(Listing, pk=listing_id)
    cart = _get_cart(request)

    # Get or create the cart item
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
    )

    # If the item was already in the cart, increment its quantity
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    # Redirect back to the listing detail page
    return redirect('listing', listing_id=listing_id)

def view_cart(request):
    """View to display the cart contents."""
    cart = _get_cart(request)
    context = {
        'cart': cart
    }
    return render(request, 'clothesshop/cart_detail.html', context)
