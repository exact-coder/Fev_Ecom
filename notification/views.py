from django.shortcuts import render,redirect
from notification.models import UserObj,Notification
from django.http import HttpResponseRedirect

# Create your views here.

def seenNotification(request,pk):
    if request.user.is_authenticated:
        user_obj = UserObj.objects.get(user=request.user)
        notification_qs = Notification.objects.get(id=pk)
        notification_qs.userobj.remove(user_obj)
        notification_qs.is_read = True
        notification_qs.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('login')
