from django.contrib import admin
from .models import Order

@admin.register(Order)
class ProductAdmin(admin.ModelAdmin):
    pass
# Register your models here.