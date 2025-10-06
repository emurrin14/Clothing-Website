from django.contrib import admin
from .models import Listing, ListingImage, Cart, CartItem, Sale, Stock


class ListingImageInline(admin.TabularInline):
    model = ListingImage
    extra = 1  # Number of extra empty forms to display

class ListingAdmin(admin.ModelAdmin):
    inlines = [ListingImageInline]


admin.site.register(Listing, ListingAdmin)
admin.site.register(Sale)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Stock)
admin.site.register(ListingImage)