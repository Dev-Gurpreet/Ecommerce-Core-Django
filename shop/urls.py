from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name="home"),
    path('shop/',views.shop, name="shop"),
    path('cart/',views.cart, name="cart"),
    path('checkout/',views.checkout, name="checkout"),
    path('update_item/',views.UpdateItem, name="update_item"),
    path('process_order/',views.processOrder, name="process_order"),
    path('gallery/',views.gallery, name="gallery"),
]


