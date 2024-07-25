from django.contrib import admin
from app_social.models import *


class ProfileAdmin(admin.ModelAdmin):
  pass


class VoteAdmin(admin.ModelAdmin):
  pass

class FriendsGroup(admin.ModelAdmin):
  pass

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Image, VoteAdmin)
admin.site.register(UserPost, FriendsGroup)