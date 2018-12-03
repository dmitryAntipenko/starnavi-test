from django.contrib.auth.models import User
from rest_framework import viewsets
from socnetapi.serializers import UserSerializer, PostSerializer
from socnetapi.models import Post


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('timestamp')
    serializer_class = PostSerializer
