from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("listing/<int:listing_id>/", views.listing, name="listing"),
    path("cart/", views.view_cart, name="view_cart"),
    path("cart/remove/<int:item_id>/", views.remove_from_cart, name="remove_from_cart"),
    path("cart/add/<int:listing_id>/", views.add_to_cart, name="add_to_cart"),
    path("cart/subtract/<int:item_id>/", views.subtract_from_cart, name="subtract_from_cart"),
    path("profile/", views.profile, name="profile"),
]