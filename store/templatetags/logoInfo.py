from django import template

from store.models import Logo,Favicon

register = template.Library()

@register.filter
def logo(user):
    logo = Logo.objects.filter(user=user,is_active=True).order_by('-id').first()
    return logo.image.url

@register.filter
def favicon(user):
    favicon = Favicon.objects.filter(user=user,is_active=True).order_by('-id').first()
    return favicon.image.url