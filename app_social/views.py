from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from datetime import datetime
from .models import Profile, Image, UserPost
from .serializers import ProfileSerializer, ImageSerializer, UserPostSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    serializer = ProfileSerializer(profile)
    return Response(serializer.data)

@api_view(['POST']) 
@permission_classes([AllowAny])
def create_user(request):
    user = User.objects.create(
        username=request.data['username']
    )
    user.set_password(request.data['password'])
    user.save()
    profile = Profile.objects.create(
        user=user,
        first_name=request.data['first_name'],
        last_name=request.data['last_name']
    )
    profile.save()
    profile_serialized = ProfileSerializer(profile)
    return Response(profile_serialized.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def create_image(request):
    image_serialized = ImageSerializer(data=request.data)
    if image_serialized.is_valid():
        image_serialized.save()
        return Response(image_serialized.data, status=status.HTTP_201_CREATED)
    return Response(image_serialized.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_images(request):
    images = Image.objects.all()  # Optionally, filter images by user or other criteria
    image_serializer = ImageSerializer(images, many=True)
    return Response(image_serializer.data)




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_user_post(request):
    print('print user Post ')
    print('user ino **********************************', request.user)
    image_id = Image.objects.get(id=request.data['image'])
    user_post = UserPost.objects.create(
        user = request.user,
        title = request.data['title'],
        text = request.data['text'],
        image = image_id,
        created_at = datetime.now()
    )
    # user = request.user
    # data = {
    #     'user': user,
    #     'title': request.data.get('title'),
    #     'text': request.data.get('text'),
    #     'image': request.data.get('image')
    # }
    # print('user ********************  ', user)
    # print('data******************* ', data)
    serializer = UserPostSerializer(user_post)
    # if serializer.is_valid():
    # serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_post(request, post_id):
    user_post = get_object_or_404(UserPost, id=post_id, user=request.user)
    serializer = UserPostSerializer(user_post, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_posts(request):
    posts = UserPost.objects.all()
    post_serializer = UserPostSerializer(posts, many=True)
    return Response(post_serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_own_posts(request):
    posts = UserPost.objects.filter(user = request.user)
    post_serializer = UserPostSerializer(posts, many=True)
    return Response(post_serializer.data)


@api_view(['GET', 'PUT', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
class UserPostViewSet(viewsets.ModelViewSet):
    queryset = UserPost.objects.all()
    serializer_class = UserPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_post(request):
    post = UserPost.objects.get(id=request.data['id'])
    post.delete()
    return Response()

