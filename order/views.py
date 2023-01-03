from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone

from store.models import Product
from order.models import Cart, Order

from coupon.models import Coupon
from coupon.forms import CouponCodeForm
# Create your views here.


def add_to_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_item = Cart.objects.get_or_create(item=item, user = request.user, purchased = False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            size = request.POST.get('size')
            color = request.POST.get('color')
            quantity = request.POST.get('quantity')
            if quantity:
                order_item[0].quantity += int(quantity)
            else:
                order_item[0].quantity += 1
            order_item[0].size = size
            order_item[0].color = color
            order_item[0].save()
            return redirect("HomePage")
        else:
            size = request.POST.get('size')
            color = request.POST.get('color')
            order_item[0].size = size
            order_item[0].color = color
            order.orderitems.add(order_item[0])
            return redirect("HomePage")
    else:
        order = Order(user=request.user)
        order.save()
        order.orderitems.add(order_item[0])
        return redirect("HomePage")


def cart_view(request):
    shipping = 5
    carts = Cart.objects.filter(user=request.user, purchased=False)
    orders = Order.objects.filter(user=request.user, ordered=False)
    if carts.exists() and orders.exists():
        order = orders[0]
        coupon_form = CouponCodeForm(request.POST)
        if coupon_form.is_valid():
            current_time = timezone.now()
            code = coupon_form.cleaned_data.get('code')
            if code:
                coupon_obj = Coupon.objects.get(code=code)
                print('coupon_obj: ',coupon_obj)
                if coupon_obj.valid_to >= current_time :
                    get_discount = (coupon_obj.discount /100) * order.get_totals()
                    total_price_after_discount = order.get_totals() - get_discount
                    discount_total_with_shipping = total_price_after_discount + shipping
                request.session['discount_total'] = total_price_after_discount
                request.session['discount_totals'] = discount_total_with_shipping
                request.session['coupon_code'] = code
                return redirect('cartview')

        coupon_code = request.session.get('coupon_code')
        discount_total = request.session.get('discount_total')
        discount_total_with_shipping = request.session.get('discount_totals')
        print("discount_total",discount_total)


        context = {
            'carts': carts,
            'order': order,
            'coupon_form': coupon_form,
            'coupon_code':coupon_code,
            'total_price_after_discount':discount_total,
            'discount_total_with_shipping': discount_total_with_shipping,
        }
        return render(request, 'store/cart.html',context)
    else:
        return ValueError("You Haven't an Active Cart !!")

def remove_item_from_cart(request,pk):
    item = get_object_or_404(Product,pk=pk)
    orders = Order.objects.filter(user=request.user, ordered=False)
    if orders.exists():
        order = orders[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item, user = request.user, purchased=False)[0]
            order.orderitems.remove(order_item)
            order_item.delete()
            return redirect('cartview')
    else:
        return ValueError("Unable to Delete!!")

def increase_cart(request,pk):
    item = get_object_or_404(Product,pk =pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item,user=request.user, purchased=False)[0]
            if order_item.quantity >= 1:
                order_item.quantity += 1
                order_item.save()
                return redirect('cartview')
            else:
                return redirect('cartview')
        else:
            return redirect('cartview')

def decrease_cart(request,pk):
    item = get_object_or_404(Product,pk =pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item,user=request.user, purchased=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                return redirect('cartview')
            else:
                order.orderitems.remove(order_item)
                order_item.delete()
                return redirect('cartview')
        else:
            return redirect('cartview')

