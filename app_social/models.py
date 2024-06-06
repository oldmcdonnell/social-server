from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    title = models.TextField()
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title if self.title else "Untitled Image"

class UserPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post', null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='user_posts', null=True, blank=True)
    no_of_like = models.IntegerField(default=0)

    def __str__(self):
        return self.title if self.title else "Untitled Post"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    comments = models.ForeignKey(UserPost, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
