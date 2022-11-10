from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category,Product

# Create your views here.
class HomeListView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'components/products/productDetail.html'
    context_object_name = 'prodDetails'
