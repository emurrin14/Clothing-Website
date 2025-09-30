from django.contrib import admin

# Register your models here.
from .models import Listing, Sale, Cart, CartItem

admin.site.register(Listing)
admin.site.register(Sale)
admin.site.register(Cart)
admin.site.register(CartItem)
