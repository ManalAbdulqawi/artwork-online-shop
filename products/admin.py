from django.contrib import admin
from .models import Product, Category, Image

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'size',
        'original_art',

    )

    ordering = ('price',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'name',
        'image',        
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Image, ImageAdmin)

