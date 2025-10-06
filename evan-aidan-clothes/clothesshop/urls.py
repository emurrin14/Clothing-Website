from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", auth_views.LoginView.as_view(template_name="clothesshop/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
    path("listing/<int:listing_id>/", views.listing, name="listing"),
    path("cart/", views.view_cart, name="view_cart"),
    path("cart/remove/<int:item_id>/", views.remove_from_cart, name="remove_from_cart"),
    path("cart/add/<int:listing_id>/", views.add_to_cart, name="add_to_cart"),
    path("cart/subtract/<int:item_id>/", views.subtract_from_cart, name="subtract_from_cart"),
    path("profile/", views.profile, name="profile"),
    path('register/', views.register, name='register'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path("instagram/", views.instagram, name="instagram"),
    path("tiktok/", views.tiktok, name="tiktok"),
    path("discord/", views.discord, name="discord"),
    path("about/", views.about, name="about"),
    path("delete_my_account/", views.delete_my_account, name="delete_my_account"),
    path('delete_account/', views.delete_user, name='delete_account'),
    path('orders/', views.orders, name='orders'),

]