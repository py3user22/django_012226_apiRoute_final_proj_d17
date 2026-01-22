from django.urls import path
from ..cart.views import add_to_cart

app_name = 'cart'

urlpatterns = [
    path('add/', add_to_cart, name="add_2cart"),
]