from django import template
from store.models import Category
from order.models import Cart,Order
register = template.Library()


@register.filter
def category(user):
    # if user.is_authenticated:
    cate = Category.objects.filter(parent=None)
    return cate
    # else:
        # return f"You are not register user"

@register.filter
def cart_count(user):
    order = Order.objects.filter(user=user, ordered=False)
    if order.exists():
        return order[0].orderitems.count()
    else:
        return 0