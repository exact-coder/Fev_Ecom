from django.urls import path
from order import views


urlpatterns = [
    path("add-to-cart/<int:pk>/",views.add_to_cart, name="addToCart"),
    path('cart/', views.cart_view, name='cartview'),
]
