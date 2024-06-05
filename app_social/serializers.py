from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, UserPost, Image

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True) 
    comments = serializers.PrimaryKeyRelatedField(queryset=UserPost.objects.all(), many=False, allow_null=True) 

    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'last_name', 'user', 'comments']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class UserPostSerializer(serializers.ModelSerializer):
    user = UserSerializer()  
    image = ImageSerializer() 

    class Meta:
        model = UserPost
        fields = ['id', 'user', 'title', 'text', 'created_at', 'image']
