"""
URL configuration for project_social project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
  TokenObtainPairView,
  TokenRefreshView,
)
from app_social.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-image/', create_image),
    path('get-images/', get_images),
    path('get-posts/', get_posts),
    path('get-own-posts/', get_own_posts),
    path('profile/', get_profile),
    path('create-user/', create_user),
    path('posts/create/', create_user_post),
    path('posts/delete/', delete_post),
    path('posts/update/<int:post_id>/', update_post, name='update_post'),
    path('refresh/', TokenRefreshView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
]

# Serve media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static(settings.MEDIA_URL, document_root='/mnt/volume_mount/media')
