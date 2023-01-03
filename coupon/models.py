from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Coupon(models.Model):
    code = models.CharField(_("Coupon Code"), max_length=50,unique=True)
    valid_from = models.DateTimeField(_("Coupon Start Time"), auto_now=False, auto_now_add=False)
    valid_to = models.DateTimeField(_("Coupon End Time"), auto_now=False, auto_now_add=False)
    discount = models.IntegerField(_("Persentage of Discount"),validators=[MinValueValidator(1),MaxValueValidator(80)])
    active = models.BooleanField(_("Coupon Code Active or Not"))

    class Meta:
        verbose_name = "Coupon Code"
    
    def __str__(self) -> str:
        return self.code

