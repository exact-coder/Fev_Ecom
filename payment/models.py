from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
# Create your models here.

class BillingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(_("First Name"), max_length=50,null=True,blank=True)
    last_name = models.CharField(_("First Name"), max_length=50,null=True,blank=True)
    country = CountryField()
    address = models.TextField(_("Address"))
    city = models.CharField(_("City"),max_length=50,null=True,blank=True)
    zipcode =models.CharField(_("Zip Code"), max_length=50,null=True,blank=True)
    phone_number = models.CharField(_("Phone Number"), max_length=16)

    def __str__(self) -> str:
        return f"{self.user.username}'s Billing Information"

    def is_fully_filled(self):
        field_names = [f.name for f in self._meta.get_fields()]
        print("field_names",field_names)
        for field_name in field_names:
            value = getattr(self, field_name)
            print("value",value)
            if value is None or value == "":
                return False
        return True


