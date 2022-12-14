from django import template
from store.models import Category

register = template.Library()


@register.filter
def category(user):
    # if user.is_authenticated:
    cate = Category.objects.filter(parent=None)
    return cate
    # else:
        # return f"You are not register user"