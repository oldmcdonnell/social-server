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
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from . import views
from app_social.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-image/', create_image),
    path('get-images/', get_images),
    path('profile/', get_profile),
    path('posts/create/',create_user_post),
    path('posts/update/<int:post_id>/', update_post, name='update_post'),
]
