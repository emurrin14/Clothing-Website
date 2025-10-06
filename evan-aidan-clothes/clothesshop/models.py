from django.db import models
from django.conf import settings


class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, default="active")

    def primary_image(self):
        """Returns the first image associated with this listing, or None."""
        first_image = self.images.first()
        return first_image.image if first_image else None


class ListingImage(models.Model):
    """An image associated with a listing."""
    listing = models.ForeignKey(Listing, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"Image for {self.listing.title}"

class Sale(models.Model):
    """Represents a site-wide sale event."""
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} (Active: {self.is_active})"
    
class Stock(models.Model):
    """Manages stock for a specific size of a listing."""
    listing = models.ForeignKey(Listing, related_name='stock_items', on_delete=models.CASCADE)
    size = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('listing', 'size')

    def __str__(self):
        return f"{self.listing.title} - Size: {self.size} ({self.quantity} in stock)"


class Cart(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    session_key = models.CharField(max_length=40, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart {self.pk} for {self.user or self.session_key}"

    def total_price(self):
        return sum(item.subtotal() for item in self.items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        related_name="items",
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(Listing, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)
    size = models.CharField(max_length=20, blank=True, null=True)


    class Meta:
        unique_together = ("cart", "product", "size")

    def __str__(self):
        return f"{self.quantity} x {self.product.title} in Cart {self.cart.pk}"

    def subtotal(self):
        return self.product.price * self.quantity