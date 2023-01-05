from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

from payment.models import BillingAddress
from payment.forms import BillingAddressForm
from order.models import Cart,Order

# Create your views here.
class CheckoutTempleteView(TemplateView):
    def get(self, request, **args):
        saved_address = BillingAddress.objects.get_or_create(user=request.user or None)
        saved_address = saved_address[0]
        form = BillingAddressForm(instance=saved_address)

        order_qs = Order.objects.filter(user=request.user, ordered=False)
        order_item = order_qs[0].orderitems.all()
        order_total = order_qs[0].get_totals()
        order_total_shipping = order_qs[0].get_totals_shipping()
        context = {
            'billing_address': form,
            'order_item':order_item,
            'order_total': order_total,
            'order_total_shipping':order_total_shipping,
        }

        return render(request, 'store/checkout.html',context)

    def post(self,request,**args):
        pass