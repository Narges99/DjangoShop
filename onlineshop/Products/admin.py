from django.contrib import admin
from Products.models import Category , Product
# Register your models here.


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['upc', 'name', 'price', 'stock' ]
    search_fields = ['upc', 'name']


admin.site.register(Category)
admin.site.register(Product, ProductsAdmin)
