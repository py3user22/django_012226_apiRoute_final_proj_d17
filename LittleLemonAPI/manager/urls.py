from django.urls import path
from . import views


# 012226' needs edits --

urlpatterns = [
    path('', views.home1, name='home'),

    # POST CALL to 'api/groups/manager/users'
    path('managers/', views.list_managers, name='list_managers'),

    # POST CALL to 'api/menu-items/'
    path('menu-items/', views.menu_items, name='menu_items'),
    path('menu-items/<int:pk>/', views.single_item, name='single_item'),

    path('menu-items-manager/<int:pk>/', views.single_item_manager, name='single_item_manager'),

    # GET CALL to 'categories/'
    path('categories/', views.category_list, name='category_list'),
    path('categories/<slug:slug>/', views.category_detail, name='category_detail'),

    # POST CALL to 'auth/token/login/'
    path('auth/token/login/', views.token_login, name='token_login'),

    # POST CALL to /delivery-crew/add/
    path('delivery-crew/add/', views. add_user_to_delivery_crew, name='add_user_to_delivery_crew'),

]