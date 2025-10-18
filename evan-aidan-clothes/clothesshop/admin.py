from django.contrib import admin, messages
from .models import Listing, ListingImage, Cart, CartItem, Sale, Stock, Subscriber
from clothes.emails import send_sale_email  # our helper function
from django.utils.translation import gettext_lazy as _
from taggit.models import Tag


class TagListFilter(admin.SimpleListFilter):
    title = _('tag')  # Display name in admin
    parameter_name = 'tag'

    def lookups(self, request, model_admin):
        tags = Tag.objects.all()
        return [(tag.id, tag.name) for tag in tags]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(tags__id=self.value())
        return queryset



# --- Listing admin setup ---
class ListingImageInline(admin.TabularInline):
    model = ListingImage
    fields = ('image', 'order')
    extra = 1

class ListingAdmin(admin.ModelAdmin):
    inlines = [ListingImageInline]
    list_display = ('title', 'price', 'status',)
    list_filter = (TagListFilter, 'status')

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
