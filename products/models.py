# Python
import random
# Django
from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
# Django signals
from django.db.models.signals import pre_save, post_save
# Django Files Storage
from django.core.files.storage import FileSystemStorage
# Django Translation
from django.utils.translation import gettext as _
from django.utils.translation import ugettext_lazy as _l

# Opciones para medir el peso
WIGTH_CHOICES	= [
        ('oz', _l('Oz')),
		('gr', _l('Gram')),
		('kg', _l('Kilogram')),
	]
# Opciones para medir el volumen
VOLUME_CHOICES	= [
		('cc', _l('Cubic centimeter')),
        ('ml', _l('Mililiter')),
		('lt', _l('Liter')),
        ('gal', _l('Gallon')),
	]

# Opciones para medir la comida
MEASURE_FOOD_CHOICES = [
        ('box', _l('Box')),
        ('package', _l('Package')),
        ('sack', _l('Sack')),
		('unity', _l('Unity')),
		('volume', VOLUME_CHOICES),
		('weight', WIGTH_CHOICES),
	]

VEGETABLES_CHOICES = [
        ('bulbs', _l('bulbs')),
        ('flowers', _l('flowers')),
        ('fruits',_l('Fruits')),
        ('leaves', _l('Leaves')),
        ('roots', _l('Roots')),
        ('seeds', _l('Seeds')),
        ('stems', _l('Stems')),
        ('tubers', _l('Tubers')),
    ]
MEATS_CHOICES = [
    ('fish',_l('Fish')),
    ('chicken',_l('Chicken')),
    ('meat_beef',_l('Beef')),
    ('meat_pork',_l('Pork meat')),
]

CATEGORY_CHOICES = [
    ('vegetables', VEGETABLES_CHOICES),
    ('fruits',_l('Fruits')),
    ('meats', MEATS_CHOICES),
    ('drinks',_l('Sport drinks')),
    ('drinks_sports',_l('Sport drinks')),
    ('cleaning_p',_l('Cleaning product')),
    ('cleaning_p_p',_l('Personal cleaning products')),
    ('other',_l('Other')),
]

class ProductName(models.Model):
    name        = models.CharField(verbose_name=_l('Product Name'), max_length=250)
    category    = models.CharField(verbose_name=_l('Category'), max_length=250, choices=CATEGORY_CHOICES, default='other')
    
    class meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    title               = models.CharField(verbose_name=_l('Title'), max_length=120)
    slug                = models.SlugField(null=True, blank=True, unique=True)
    description         = models.TextField(verbose_name=_l('Description'))
    price               = models.DecimalField(
                        verbose_name=_l('Price'), 
                        decimal_places=2, 
                        max_digits=20, 
                        default=10)
    price_offer         = models.DecimalField(
                        verbose_name=_l('Price'), 
                        decimal_places=2, 
                        max_digits=20,
                        null = True,
                        blank=True)
    quantity            = models.IntegerField(verbose_name=_l('Quantity'), default=0)
    quantity_available  = models.IntegerField(verbose_name=_l('Quantity available'), default=1)
    image               = models.ImageField(
                        verbose_name=_l('Image'), 
                        null=True, 
                        blank=True)
    featured            = models.BooleanField(verbose_name=_l('Featured'), default=False)
    active              = models.BooleanField(verbose_name=_l('Active'), default=True)
    updated 	        = models.DateTimeField(
						auto_now=True, 
						auto_now_add=False,
						verbose_name=_l('Update date'))
    timestamp 	        = models.DateTimeField(
						auto_now=False, 
						auto_now_add=True,
						verbose_name=_l('Creation date'))

    # objects = ProductManager()

    class Meta:
        verbose_name=_('Product')
        verbose_name_plural = _('Products')
        ordering = ('price','timestamp')

    # def get_absolute_url(self):
    #     #return "/products/{slug}/".format(slug=self.slug)
    #     return reverse("products:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    # @property
    # def name(self):
    #     return self.title

    # def get_downloads(self):
    #     qs = self.productfile_set.all()
    #     return qs


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug or instance.title:
        print("pre save")
        instance.slug = slugify(instance.title, allow_unicode=True)
pre_save.connect(product_pre_save_receiver, sender=Product)

def product_post_save_receiver(sender, instance, created, *args, **kwargs):
    if created:
        print("Create post save")
        if not instance.slug or instance.title:
            print("post save")
            instance.slug = slugify(instance.title, allow_unicode=True)
            instance.save()
post_save.connect(product_post_save_receiver, sender=Product)

class ProductProvider(models.Model):
    product_name        = models.ForeignKey(
                        ProductName, 
                        verbose_name=_("Product name"), 
                        on_delete=models.CASCADE) 
    measure_food        = models.CharField(
                        verbose_name=_l('Type measure food'), 
                        max_length=256,
                        choices = MEASURE_FOOD_CHOICES,)
    quantity            = models.IntegerField(verbose_name=_l('Quantity'), default=1)
    price_unitary     = models.DecimalField(
                        verbose_name=_l('Price by unit'), 
                        decimal_places=2, 
                        max_digits=20, 
                        default=10)
    price_subtotal    = models.DecimalField(
                        verbose_name=_l('Subtotal'), 
                        decimal_places=2, 
                        max_digits=20,
                        null = True,
                        blank = True)
    
    class Meta:
        verbose_name=_('Products of provider')
        verbose_name_plural = _('Products of providers')
    
    def __str__(self):
        return self.product_name.name

def product_provider_pre_save_receiver(sender, instance, *args, **kwargs):
    if instance.price_unitary:
        instance.price_subtotal = instance.price_unitary * instance.quantity
pre_save.connect(product_provider_pre_save_receiver, sender=ProductProvider)

def product_provider_post_save_receiver(sender, instance, created, *args, **kwargs):
    if created:
        if instance.price_unitary:
            instance.price_subtotal = instance.price_unitary * instance.quantity
            instance.save()
post_save.connect(product_provider_post_save_receiver, sender=ProductProvider)