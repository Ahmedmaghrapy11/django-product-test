from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission
from .models import Product
# Register your models here.
admin.site.register(Product)
