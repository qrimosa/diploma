from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'size', 'get_product_image', 'category')
    list_display_links = ('category', 'name')
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('name', 'color')}

    def get_product_image(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=70")
    
    get_product_image.short_description = 'Зображення'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_category_image')
    list_display_links = ('name', )
    prepopulated_fields = {'slug': ('name',)}
    
    def get_category_image(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=70")
        
    get_category_image.short_description = 'Зображення'


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
