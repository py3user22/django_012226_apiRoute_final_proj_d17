from django.urls import path
from ..menu.views import menu_items, single_item, category_detail, category_list


app_name = 'menu'

urlpatterns = [
    path('menu-items/', menu_items, name='menu-items'),
    path('menu-items/<int:pk>/', single_item, name='single-items'),
    # GET CALL to 'categories/'
    path('categories/', category_list, name='category-list'),
    path('categories/<slug:slug>/', category_detail, name='category_detail'),

]
