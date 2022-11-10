from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(_("Category Name"), max_length=150,blank=False, null=False)
    image = models.ImageField(_("Category Logo"), upload_to="category/",blank=True, null=True)
    parent = models.ForeignKey("self",related_name='children',on_delete=models.CASCADE,blank=True,null=True,verbose_name=_("children"))
    created = models.DateTimeField(_("Creation date"), auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['-created',]
        verbose_name_plural = 'Categories'

class Product(models.Model):
    name = models.CharField(_("Product Name"), max_length=150)
    slug = models.SlugField(_(""),unique=True)
    category = models.ForeignKey(Category, verbose_name=_("category"),related_name='category', on_delete=models.CASCADE)
    preview_des = models.CharField(_("Short Description"), max_length=500,blank=True,null=True)
    description = RichTextField(_("Description"))
    image = models.ImageField(_("Product Image"), upload_to="products/")
    price = models.FloatField(_("Product Price"))
    old_price = models.FloatField(_("Product Old Price"),blank=True,null=True)
    is_stock = models.BooleanField(_("Poduct available or not"),default=True)
    created = models.DateTimeField(_("Date"), auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['-created',]
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def get_product_url(self):
        return reverse('productDetails', kwargs={'slug': self.slug})

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
