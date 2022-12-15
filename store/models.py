from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField

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
    category = models.ForeignKey(Category, verbose_name=_("category"),related_name='category', on_delete=models.CASCADE)
    preview_des = models.CharField(_("Short Description"), max_length=500,blank=True,null=True)
    description = RichTextField(_("Description"))
    image = models.ImageField(_("Product Image"), upload_to="products/")
    price = models.FloatField(_("Product Price"))
    old_price = models.FloatField(_("Product Old Price"),blank=True,null=True)
    is_stock = models.BooleanField(_("Poduct available or not"),default=True)
    slug = AutoSlugField(populate_from='name', unique=True, always_update=True)
    created = models.DateTimeField(_("Date"), auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['-created',]
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.FileField(_("Gallery Image"), upload_to='product_gallery/')
    created = models.DateTimeField(_("Uploding time"), auto_now_add=True)

    def __str__(self) -> str:
        return str(self.product.name)

class VariationManager(models.Manager):
    def sizes(self):
        return super(VariationManager, self).filter(variation="size")
    def colors(self):
        return super(VariationManager, self).filter(variation="color")

VARIATIONS_TYPE = (
    ('size', 'size'),
    ('color', 'color'),
)

class VariationValue(models.Model):
    variation = models.CharField(_("Variation Type"), max_length=100, choices=VARIATIONS_TYPE)
    name = models.CharField(_("Variation Name"), max_length=100)
    product = models.ForeignKey(Product, verbose_name=_("product"), on_delete=models.CASCADE)
    price = models.IntegerField(_("Variation Product Size"),blank=True,null=True)
    created = models.DateTimeField(_(""), auto_now=False, auto_now_add=True)

    objects = VariationManager()

    def __str__(self) -> str:
        return self.name