from django.contrib import admin
from .models import Client, Product, Order


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'address', 'registration_date']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'quantity', 'added_date', 'photo']


class ProductInline(admin.TabularInline):
    model = Product
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'total_amount', 'order_date']
    inlines = [ProductInline]


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
