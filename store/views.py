from django.shortcuts import render
from django.views.generic import ListView, DetailView,TemplateView
from .models import Category,Product,ProductImages,Banner,Offer

# Create your views here.
class HomeListView(TemplateView):

    def get(self,request,**kwargs):
        products = Product.objects.all().order_by('-id')
        featured_products = Product.objects.filter(product_variatin='Featured Products').order_by('-id')[0:8]
        recent_products = Product.objects.filter(product_variatin='Recent Products').order_by('-id')[0:8]
        most_view_products = Product.objects.filter(product_variatin='Most View Products').order_by('-id')[0:8]
        banners = Banner.objects.filter(is_active=True).order_by('-id')[0:4]
        offers = Offer.objects.filter(is_active=True).order_by('-id')[0:2]

        context={
            'products':products,
            'featured_products': featured_products,
            'recent_products': recent_products,
            'most_view_products': most_view_products,
            'banners': banners,
            'active_banner': len(banners),
            'offers':offers,
        }
        return render(request, 'index.html',context)


    def post(self,request, **kwargs):
        if request.method == 'post' or request.method =='POST':
            search_product = request.POST.get('search_product')
            products = Product.objects.filter(name__icontains=search_product).order_by('-id')

            context = {
                'products': products
            }
            return render(request, 'index.html',context)

def allProduct(request):
    products = Product.objects.all().order_by('-id')
    context ={
        'products':products,
    }
    return render(request,'components/products/allProduct.html',context)

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