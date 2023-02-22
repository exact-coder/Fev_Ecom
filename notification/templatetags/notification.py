from django import template
from notification.models import UserObj,Notification


register = template.Library()

@register.filter
def notifications(user):
    if user.is_authenticated:
        user_obj = UserObj.objects.get(user=user)
        notification = Notification.objects.filter(userobj= user_obj,is_read=False).order_by('-id')
        if notification.exists():
            return notification
        else:
            return 0
    else:
        return None
    
@register.filter
def read_notifications(user):
    if user.is_authenticated:
        user_obj = UserObj.objects.get(user=user)
        read_notification = Notification.objects.filter(userobj= user_obj,is_read=True).order_by('-id')
        if read_notification.exists():
            return read_notification
        else:
            return 0
    else:
        return None


@register.filter
def notification_count(user):
    if user.is_authenticated:
        user_obj = UserObj.objects.get(user=user)
        notification = Notification.objects.filter(userobj= user_obj)
        if notification.exists():
            return notification.count()
        else:
            return 0
    else:
        return 0