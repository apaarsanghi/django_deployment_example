from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)

    #additional info
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    #blank= true means the field is optional
    #upload_to is the folder name inside the media folder
    def __str__(self):
        return self.user.username

    #user.username -> user is the variable defined above which has a relationship with the User Model
    #.username is the attribute of that Model


class DrumsModel(models.Model):
    drums_model = models.CharField(max_length=200, unique=True)
    drums_brand = models.CharField(max_length=200)
    drums_year = models.DateField()

    def __str__(self):
        return self.drums_model


class DrumsStore(models.Model):
    drums_model = models.ForeignKey(DrumsModel, on_delete=models.CASCADE)
    drums_store = models.CharField(max_length=200)
    drums_units = models.IntegerField()

    def __str__(self):
        return self.drums_store


class DrumsCost(models.Model):
    drums_model = models.ForeignKey(DrumsModel, on_delete=models.CASCADE)
    drums_store = models.ForeignKey(DrumsStore, on_delete=models.CASCADE)
    drums_address = models.CharField(max_length=200, unique=True)
    drums_cost = models.IntegerField()

    def __str__(self):
        return str(self.drums_cost)


# class DrumsSearch(models.Model):
#     drums_model = models.CharField(max_length=200, unique=True)
#
#     def __str__(self):
#         return self.drums_model



