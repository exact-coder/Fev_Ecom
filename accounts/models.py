from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("Profile"),related_name="profile", on_delete=models.CASCADE)
    full_name = models.CharField(_("Full Name"), max_length=150,null=True,blank=True)
    address=models.TextField(_("Adderss"),null=True,blank=True)
    country = models.CharField(_("Country Name"), max_length=150,null=True,blank=True)
    city = models.CharField(_("City Name"), max_length=150,null=True,blank=True)
    zipcode = models.CharField(_("Zipcode"), max_length=15,null=True,blank=True)
    phone = models.CharField(_("Phone"), max_length=15,null=True,blank=True)
    date_joined = models.DateTimeField(_("Joined Date"),auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
