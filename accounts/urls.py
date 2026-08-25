from django.urls import path
from . import views


urlpatterns = [
    path("", views.landing, name="landing"),
    path("home/", views.home, name="home"),

    # Authentication
    path("login/", views.login_view, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_view, name="logout"),

    # Booking
    path("form/", views.booking_form, name="booking"),
    path("bookings/", views.booking_list, name="booking_list"),
    path("edit/<int:id>/", views.edit_booking, name="edit_booking"),
    path("delete/<int:id>/", views.delete_booking, name="delete_booking"),
]