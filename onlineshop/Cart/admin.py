from django.contrib import admin

from Cart.models import Cart, CartLine


# Register your models here
# .
class CartLineInLine(admin.TabularInline):
    model = CartLine
    extra = 1


class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_time']
    inlines = (CartLineInLine , )

admin.site.register(Cart , CartAdmin)