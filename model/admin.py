from django.contrib import admin
from .models import Customer, Order, OrderItem, Product, ShippingAddress, Category, User


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_display_links = ['name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']
    list_display_links = ['name']


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'address', 'city', 'country')
    list_display_links = ('user', )


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'created_at', 'paid']
    list_display_links = ('customer', )


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity']
    list_display_links = ('order', 'product')


class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['customer', 'address', 'city', 'postal_code']



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
