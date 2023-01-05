from django.urls import path
from payment import views


urlpatterns = [
    path("checkout/",views.CheckoutTempleteView.as_view(),name='checkout'),
]






