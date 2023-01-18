from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

# Create your models here.

class CustomManager(BaseUserManager):
    def create_user(self, email,user_name,password, **extra_fields):
        if not email:
            raise ValueError("Valid Email Must be Given")
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, user_name, password, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_verify',True)
        extra_fields.setdefault('user_type', 'owner')


        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser must be is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must be is_superuser=True')
        if extra_fields.get('is_active') is not True:
            raise ValueError('superuser must be is_active=True')
        if extra_fields.get('is_verify') is not True:
            raise ValueError('superuser must be is_verify=True')

        return self.create_user(email,user_name,password,**extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    USER_TYPE = (
        ('visitor','visitor'),
        ('owner','owner'),
        ('admin','admin'),
        ('manager','manager'),
        ('developer','developer'),
    )
    email = models.EmailField(_("Email"), max_length=254, unique=True)
    user_name = models.CharField(_("User Name"), max_length=150,unique=True)
    REQUIRED_FIELDS = ['user_name']
    USERNAME_FIELD = 'email'
    user_type = models.CharField(_("User Type"), max_length=100,choices=USER_TYPE, default=USER_TYPE[0])
    is_staff = models.BooleanField(_("Is Staff"),default=False)
    is_superuser = models.BooleanField(_("Is Superuser"),default=False)
    is_active = models.BooleanField(_("Is Active"),default=False)
    is_verify = models.BooleanField(_("Is Verify"),default=False)

    objects = CustomManager()

    def __str__(self) -> str:
        return str(self.email)

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("Profile"),related_name="profile", on_delete=models.CASCADE)
    full_name = models.CharField(_("Full Name"), max_length=150,null=True,blank=True)
    address=models.TextField(_("Adderss"),null=True,blank=True)
    country = CountryField()
    city = models.CharField(_("City Name"), max_length=150,null=True,blank=True)
    zipcode = models.CharField(_("Zipcode"), max_length=15,null=True,blank=True)
    phone = models.CharField(_("Phone"), max_length=15,null=True,blank=True)
    date_joined = models.DateTimeField(_("Joined Date"),auto_now_add=True)

    def __str__(self):
        return f"{self.user.user_name}'s Profile"
    
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
