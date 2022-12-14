from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from store.models import Product

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE, related_name='cart')
    item = models.ForeignKey(Product, verbose_name=_("Product item"), on_delete=models.CASCADE)
    quantity = models.IntegerField(_("Quanftity of Product"), default=1)
    purchased = models.BooleanField(_("Purchased or Not"))
    created = models.DateTimeField(_("Adding Time"), auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(_("Update Time"), auto_now=True, auto_now_add=False)


    def __str__(self) -> str:
        return f"{self.quantity} X {self.item}"

    def get_total(self):
        total = self.item.price * self.quantity
        float_total = format(total, '0.2f')
        return float_total

class Order(models.Model):
    user = models.ForeignKey(User, verbose_name=_(""), on_delete=models.CASCADE)
    orderitems = models.ManyToManyField(Cart, verbose_name=_("Ordered Products"))
    ordered = models.BooleanField(_("Ordered"), default=False)
    created = models.DateTimeField(_("Created"), auto_now=False, auto_now_add=True)
    paymentId = models.CharField(_("Payment Id"), max_length=300,blank=True,null=True)
    orderdId = models.CharField(_("Ordered Id"), max_length=300,blank=True,null=True)
    
    def get_totals_shipping(self):
        totals = 30 
        for order_item in self.orderitems.all():
            totals += float(order_item.get_total())
        return totals

    def get_totals(self):
        total  =0 
        for order_item in self.orderitems.all():
            total += float(order_item.get_total())
        return total

    
