from django.contrib import admin

# Register your models here.
from .models import Listing, Sale

admin.site.register(Listing)
admin.site.register(Sale)
