from django.contrib import admin
from app1.models import Menu, Item, Drink, Ingredients
# Register your models here.

admin.site.register(Menu)
admin.site.register(Item)
admin.site.register(Drink)
admin.site.register(Ingredients)