from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm, RegistrationForm
from .models import Listing, Cart, CartItem
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import default_token_generator
import logging

# Create your views here.

logger = logging.getLogger('clothesshop')

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
    return redirect('view_cart')

def view_cart(request):
    """View to display the cart contents."""
    cart = _get_cart(request)
    context = {
        'cart': cart
    }
    return render(request, 'clothesshop/cart_detail.html', context)

def remove_from_cart(request, item_id):
    """View to remove an item from the cart."""
    cart_item = get_object_or_404(CartItem, pk=item_id)
    current_cart = _get_cart(request)

    # Ensure the item being removed belongs to the current user's cart
    if cart_item.cart == current_cart:
        cart_item.delete()

    # Redirect back to the cart page
    return redirect('view_cart')

def subtract_from_cart(request, item_id):
    """View to subtract an item from the cart."""
    cart_item = get_object_or_404(CartItem, pk=item_id)
    current_cart = _get_cart(request)

    # Ensure the item belongs to the current user's cart
    if cart_item.cart == current_cart:
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()

    return redirect('view_cart')


def profile(request):
    if not request.user.is_authenticated:
        return redirect('login') # Or render a login page
    
    return render(request, "clothesshop/profile.html")

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Deactivate account until email confirmation
            user.save()

            # Send activation email logic
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('clothesshop/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()

            return render(request, 'clothesshop/account_activation_sent.html')
    else:
        form = RegistrationForm()

    return render(request, 'clothesshop/register.html', {'form': form})

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('index')
    else:
        return render(request, 'clothesshop/account_activation_invalid.html')

def instagram(request):
    return redirect("https://www.instagram.com")

def tiktok(request):
    return redirect("https://www.tiktok.com")

def discord(request):
    return redirect("https://discord.gg")