from django.db import models

# Create your models here.
class Menu(models.Model):
    menu_name = models.CharField(max_length=100)

    def __str__(self):
        return self.menu_name


class Item(models.Model):
    menu_name = models.ForeignKey(Menu, on_delete=models.SET())
    item_name = models.CharField(max_length=50)
    item_description = models.CharField(max_length=100)
    item_calories = models.IntegerField()
    item_price = models.FloatField()

    def __str__(self):
        return self.item_name


class Drink(models.Model):
    drink_name = models.OneToOneField(Item,on_delete=models.CASCADE)
    drink_caffeine = models.IntegerField()

    def __str__(self):
        return str(self.drink_name)


class Ingredients(models.Model):
    item_name = models.ManyToManyField(Item,blank=True)
    ingredient_name = models.CharField(max_length=100)

    def __str__(self):
        return self.ingredient_name


