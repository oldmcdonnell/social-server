from django.contrib import admin
from app_social.models import *


class ProfileAdmin(admin.ModelAdmin):
  pass


class ImageAdmin(admin.ModelAdmin):
  pass

class UserPostAdmin(admin.ModelAdmin):
  pass

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(UserPost, UserPostAdmin)