from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin

from socnetapi.serializers import UserSerializer, PostSerializer
from socnetapi.models import Post


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class PostViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Post.objects.all().order_by('timestamp')
    serializer_class = PostSerializer

    login_url = '/auth/login/'
    redirect_field_name = 'redirect_to'
