from django.contrib import admin
from .models import Listing, Cart, CartItem, Sale, Stock


# Register your models here.
from .models import Listing, Sale, Cart, CartItem

admin.site.register(Listing)
admin.site.register(Sale)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Stock) # Add this line