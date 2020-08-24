from django.contrib import admin
from drums.models import DrumsModel, DrumsCost, DrumsStore, UserProfileInfo
# Register your models here.

admin.site.register(DrumsCost)
admin.site.register(DrumsModel)
admin.site.register(DrumsStore)
admin.site.register(UserProfileInfo)