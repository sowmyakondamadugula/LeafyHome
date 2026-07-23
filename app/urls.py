from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login_user,name='login'),
    path('signup/',views.signup,name='signup'),
    path('shop/',views.shop,name='shop'),
    path('about/',views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path("add_to_cart/<int:id>/", views.add_to_cart, name="add_to_cart"),
    path("increase/<int:id>/", views.increase_quantity, name="increase_quantity"),
    path("decrease/<int:id>/", views.decrease_quantity, name="decrease_quantity"),
    path('remove_from_cart/<int:id>/',views.remove_from_cart,name="remove_from_cart"),
    path('cart/',views.cart,name='cart'),
    path('logout/',views.logout_user,name='logout_user')
]
