from django.db import models
from django.conf import settings


class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    primary_image = models.ImageField(upload_to="images/", blank=True, null=True)
    secondary_image = models.ImageField(upload_to="images/", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, default="active")

class Sale(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    status = models.CharField(max_length=10, default="pending")

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

    class Meta:
        unique_together = ("cart", "product")

    def __str__(self):
        return f"{self.quantity} x {self.product.title} in Cart {self.cart.pk}"

    def subtotal(self):
        return self.product.price * self.quantity