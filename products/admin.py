# Django
from django.contrib import admin
# Django Translation
from django.utils.translation import gettext as _
from django.utils.translation import ugettext_lazy as _l

# Project
from .models import Product, ProductProvider

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','description','price', 'quantity',
                    'active','updated', 'timestamp',
                    ]
    fieldsets = (
        (_('Product Information'), {'fields': ('title','slug', 'description', 'price', 'quantity', 'quantity_available')}),
        (_l('Important dates'), {'fields': ('updated','timestamp')}),
        (_l('Access'), {'fields': ('active','featured', 'is_digital')}),
    )
    list_display_links  = ['title']
    list_editable       = ['active','price', 'quantity']
    readonly_fields 	= ['quantity_available', 'slug','updated','timestamp']

    class Meta:
        model = Product

class ProductProviderAdmin(admin.ModelAdmin):
    list_display = ['title','price', 'quantity', 'quantity_available', 
                    'active','updated', 'timestamp',
                    ]
    fieldsets = (
        (_('Product Information'), {'fields': ('title','slug', 'description', 'price', 'quantity', 'quantity_available')}),
        (_l('Important dates'), {'fields': ('updated','timestamp')}),
        (_l('Access'), {'fields': ('active','featured', 'is_digital')}),
        (_l('Measurements'), {'fields': ('measure_food','measure_Volume','measure_Weight')}),
    )
    list_display_links  = ['title']
    list_editable       = ['active','price','quantity_available']
    readonly_fields 	= ['slug', 'updated','timestamp']

    class Meta:
        model = ProductProvider

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductProvider, ProductProviderAdmin)