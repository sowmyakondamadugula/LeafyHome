from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(plant)
admin.site.register(Category)
admin.site.register(user_numbers)
admin.site.register(cart_items)