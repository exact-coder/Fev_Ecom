from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

User = get_user_model()

# # Create your models here.

class UserObj(models.Model):
    user = models.OneToOneField(User, related_name=_("userobj"), on_delete=models.CASCADE)
    created = models.DateTimeField(_("Created"), auto_now=False, auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.email} notification"

    @receiver(post_save, sender=User)
    def create_notification_object(sender,instance,created ,**kwargs):
        if created:
            UserObj.objects.create(user=instance)
        instance.UserObj.save()

class Notification(models.Model):
    userobj = models.ManyToManyField(UserObj, verbose_name=_("notification"),blank=True)
    message = models.TextField(_("Notification Message"))
    is_read = models.BooleanField(_("Is Read"),default=False)
    created = models.DateTimeField(_("Created"), auto_now=False, auto_now_add=True)

    def __str__(self) -> str:
        return str(self.message)