from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category,Product,ProductImages

# Create your views here.
class HomeListView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'components/products/productDetail.html'
    context_object_name = 'prodDetails'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_photos'] = ProductImages.objects.filter(product=self.object.id)
        return context

"""#For function based productdetails page
def productDetails(request,slug):
    item = Product.objects.get(id=slug)
    photos = ProductImages.objects.filter(product = item).order_by('created')
    context ={
        'singleproduct': item,
        'photos': photos,
    }
    return render(request, 'components/products/productDetail.html', context)"""