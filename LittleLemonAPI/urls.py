from django.urls import path
from . import views


urlpatterns = [
    path('', views.home1, name='home'),
    path('manage-one/', views.manage1, name='manager-html'),

]