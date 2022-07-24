from django.urls import path
from .views import StripCheckOutView

urlpatterns = [
    path('create-checkout-session',StripCheckOutView.as_view())
]
