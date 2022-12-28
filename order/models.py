from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from store.models import Product,VariationValue

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE, related_name='cart')
    item = models.ForeignKey(Product, verbose_name=_("Product item"), on_delete=models.CASCADE)
    quantity = models.IntegerField(_("Quanftity of Product"), default=1)
    size = models.CharField(_("Product Size"), max_length=100,blank=True,null=True)
    color = models.CharField(_("Product Color"), max_length=100,blank=True,null=True)
    purchased = models.BooleanField(_("Purchased or Not"))
    created = models.DateTimeField(_("Adding Time"), auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(_("Update Time"), auto_now=True, auto_now_add=False)

    def __str__(self) -> str:
        return f"{self.quantity} X {self.item}"

    def get_total(self):
        total = self.item.price * self.quantity
        float_total = format(total, '0.2f')
        return float_total

    def variation_single_price(self):
        sizes = VariationValue.objects.filter(variation="size", product=self.item)
        colors = VariationValue.objects.filter(variation="color", product=self.item)
        for size in sizes:
            if colors.exists():
                for color in colors:
                    if color.name == self.color:
                        c_price = color.price
                if size.name == self.size and c_price:
                    total = size.price + c_price
                    net_total = total
                    float_total = format(total, '0.2f')
                    return float_total
            else:
                if size.name == self.size:
                    total = size.price
                    net_total = format(total, '0.2f')
                    return net_total
    def variation_total(self):
        sizes = VariationValue.objects.filter(variation="size", product=self.item)
        colors = VariationValue.objects.filter(variation="color", product=self.item)
        for size in sizes:
            if colors.exists():
                for color in colors:
                    if color.name == self.color:
                        c_price = color.price + self.item.price
                        color_quantity_price = c_price * self.quantity
                if size.name == self.size and color_quantity_price:
                    total = color_quantity_price
                    net_total = total
                    float_total = format(total, '0.2f')
                    return float_total
            else:
                if size.name == self.size:
                    total = size.price * self.quantity
                    net_total = format(total, '0.2f')
                    return net_total



class Order(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User Name"), on_delete=models.CASCADE)
    orderitems = models.ManyToManyField(Cart, verbose_name=_("Ordered Products"))
    ordered = models.BooleanField(_("Ordered"), default=False)
    created = models.DateTimeField(_("Created"), auto_now=False, auto_now_add=True)
    paymentId = models.CharField(_("Payment Id"), max_length=300,blank=True,null=True)
    orderdId = models.CharField(_("Ordered Id"), max_length=300,blank=True,null=True)
    
    def get_totals_shipping(self):
        totals = 5 
        for order_item in self.orderitems.all():
            if order_item.variation_total():
                totals += float(order_item.variation_total())
            else:
                totals += float(order_item.get_total())
        return totals

    def get_totals(self):
        total  =0 
        for order_item in self.orderitems.all():
            if order_item.variation_total():
                total += float(order_item.variation_total())
            else:
                total += float(order_item.get_total())
        return total

