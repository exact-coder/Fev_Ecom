from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

from payment.models import BillingAddress
from payment.forms import BillingAddressForm,PaymentMethodForm
from order.models import Cart,Order

# Create your views here.
class CheckoutTempleteView(TemplateView):
    def get(self, request, **args):
        saved_address = BillingAddress.objects.get_or_create(user=request.user or None)
        saved_address = saved_address[0]
        form = BillingAddressForm(instance=saved_address)
        payment_method = PaymentMethodForm()

        order_qs = Order.objects.filter(user=request.user, ordered=False)
        order_item = order_qs[0].orderitems.all()
        order_total = order_qs[0].get_totals()
        order_total_shipping = order_qs[0].get_totals_shipping()
        context = {
            'billing_address': form,
            'order_item':order_item,
            'order_total': order_total,
            'order_total_shipping':order_total_shipping,
            'payment_method':payment_method,
        }

        return render(request, 'store/checkout.html',context)

    def post(self,request,**args):
        saved_address = BillingAddress.objects.get_or_create(user=request.user or None)
        saved_address = saved_address[0]
        form = BillingAddressForm(instance=saved_address)
        payment_obj = Order.objects.filter(user=request.user, ordered=False)[0]
        payment_form = PaymentMethodForm(instance=payment_obj)
        if request.method == 'POST' or request.method == 'post':
            form = BillingAddressForm(request.POST, instance=saved_address)
            pay_form = PaymentMethodForm(request.POST, instance=payment_obj)
            if form.is_valid() and pay_form.is_valid():
                form.save()
                pay_method = pay_form.save()
                if not saved_address.is_fully_filled():
                    return redirect('checkout')

                # Cash on Delivery Payment Process
                if pay_method.payment_method == 'Cash on Delivery':
                    order_qs = Order.objects.filter(user=request.user, ordered=False)
                    order = order_qs[0]
                    order.ordered = True
                    order.orderdId = order.id
                    order.paymentId = pay_method.payment_method
                    order.save()
                    cart_items = Cart.objects.filter(user=request.user, purchased=False)
                    for item in cart_items:
                        item.purchased = True
                        item.save()
                    return redirect('HomePage')
