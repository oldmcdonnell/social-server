from django.db import models
from django.contrib.auth.models import User

class UserPost(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_posts')
    title = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Image(models.Model):
    user_post = models.ForeignKey(UserPost, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"Image for post: {self.user_post.title}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    comments = models.ForeignKey(UserPost, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
