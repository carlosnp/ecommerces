# Django
from django.contrib import admin
# Django Translation
from django.utils.translation import gettext as _
from django.utils.translation import ugettext_lazy as _l

# Project
from .models import ProductName, Product, ProductProvider

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','description','price', 'quantity',
                    'active','updated', 'timestamp',
                    ]
    fieldsets = (
        (_('Product Information'), {'fields': ('title','slug', 'description', 'price', 'quantity', 'quantity_available')}),
        (_l('Important dates'), {'fields': ('updated','timestamp')}),
        (_l('Access'), {'fields': ('active','featured')}),
    )
    list_display_links  = ['title']
    list_editable       = ['active','price', 'quantity']
    readonly_fields 	= ['quantity_available', 'slug','updated','timestamp']

    class Meta:
        model = Product

class ProductNameAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    ordering = ['name']

    class Meta:
        model = ProductName

class ProductProviderAdmin(admin.ModelAdmin):
    list_display = ['product_name','quantity', 'measure_food', 'price_unitary', 
                    'price_subtotal'
                    ]
    ordering = ['product_name']
    readonly_fields 	= ['price_subtotal',]
    
    class Meta:
        model = ProductProvider

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductProvider, ProductProviderAdmin)
admin.site.register(ProductName, ProductNameAdmin)