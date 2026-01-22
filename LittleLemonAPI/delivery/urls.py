from django.urls import path
from ..delivery.views import delivery_list, delivery_single, delivery_create, delivery_update, assign_delivery_crew, create_delivery_crew


app_name = 'delivery'

urlpatterns = [
    path('delivery/', delivery_list, name='delivery_list'),
    path('delivery/<int:pk>/', delivery_single, name='delivery-single-view' ),

    # 011926 locked for authZ users only
    path('delivery-make', delivery_create, name='delivery-create-view' ),
    path('delivery-update/', delivery_list, name='delivery-list-view' ),
    path('delivery-update/<int:pk>', delivery_update, name='delivery-update-view' ),

    # 0120 assign new user to crew
    path('assign-crew/', assign_delivery_crew, name='assign-crew' ),
    path('create-crew/', create_delivery_crew, name='create-crew' ),


]