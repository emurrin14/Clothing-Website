from django.db import models


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

