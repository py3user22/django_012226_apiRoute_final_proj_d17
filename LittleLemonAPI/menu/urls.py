from django.urls import path
from ..menu.views import menu_items, single_item


app_name = 'menu'

urlpatterns = [
    path('menu-items/', menu_items, name='menu-items'),
    path('menu-items/<int:pk>/', single_item, name='single-items'),

]
