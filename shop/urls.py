from telnetlib import SE
from django.contrib import admin
from django.urls import path, include
from .views import ProductView, SearchView
from . import views
from user import views as user_view


urlpatterns = [
    path('', ProductView.as_view(), name='store' ),
    path('cart/', views.cart, name='cart'),
    path('single/<str:pk>', views.single, name='single'),
    path('addcart/', views.addcart, name='addcart'),
    path('checkout/', views.checkout, name='checkout'),
    path('search', SearchView.as_view(), name='search'),
    path('searching', views.searching, name='searching')
    
]