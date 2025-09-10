from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
list_display = ('name', 'price', 'available', 'created_at')
list_filter = ('available', 'created_at')
prepopulated_fields = {'slug': ('name',)}
search_fields = ('name', 'description')
