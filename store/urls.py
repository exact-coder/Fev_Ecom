from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='HomePage'),
    path('snackbar/',views.snackBar,name='snackbar'),
    path('allproduct/', views.allProduct, name='allProduct'),
    path('contract/', views.contract, name='contract'),
    path('productDetails/<slug:slug>/', views.ProductDetailView.as_view(), name='productDetails'),
]
