from django.urls import path
from order import views


urlpatterns = [
    path("add-to-cart/<int:pk>/",views.add_to_cart, name="addToCart"),
    path('cart/', views.cart_view, name='cartview'),
    path('remove-item/<int:pk>/', views.remove_item_from_cart, name='removeitem'),
    path('increase-quantity/<int:pk>/', views.increase_cart, name='increase-quantity'),
    path('decrease-quantity/<int:pk>/', views.decrease_cart, name='decrease-quantity'),
]
