from django.contrib import admin, messages
from .models import Listing, ListingImage, Cart, CartItem, Sale, Stock, Subscriber
from clothes.emails import send_sale_email  # our helper function

# --- Listing admin setup ---
class ListingImageInline(admin.TabularInline):
    model = ListingImage
    fields = ('image', 'order')
    extra = 1

class ListingAdmin(admin.ModelAdmin):
    inlines = [ListingImageInline]

# --- Sale email admin action ---
@admin.action(description="Send Sale Email to selected subscribers")
def send_sale_email_action(modeladmin, request, queryset):
    emails = list(queryset.values_list("email", flat=True))
    if not emails:
        messages.warning(request, "No subscribers selected.")
        return
    send_sale_email(emails)
    messages.success(request, f"Sale email sent to {len(emails)} subscribers!")

# --- Register models ---
admin.site.register(Listing, ListingAdmin)
admin.site.register(Sale)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Stock)
admin.site.register(ListingImage)

# --- Subscriber admin with action ---
@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "date_joined")  # adjust fields as needed
    actions = [send_sale_email_action]
