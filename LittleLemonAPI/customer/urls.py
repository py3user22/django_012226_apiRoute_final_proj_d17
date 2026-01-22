from django.urls import path
from ..customer.views import view1_menu, category_view, view2_single


app_name = 'customer'

urlpatterns = [
    path('customer-menu/', view1_menu, name='customer'),
    path('customer-menu/<int:pk>', view2_single, name='customer'),
    path('category-view/', category_view, name='category-view'),
]