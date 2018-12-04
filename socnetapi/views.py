from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import action

from socnetapi.serializers import UserSerializer, PostSerializer
from socnetapi.models import Post


class UserViewSet(PermissionRequiredMixin, viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_required = (IsAdminUser,)


class PostViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Post.objects.all().order_by('timestamp')
    serializer_class = PostSerializer

    login_url = '/auth/login/'
    redirect_field_name = 'redirect_to'

    @action(detail=True)
    def like(self, request, pk=None):
        post = self.get_object()
        post.liked.add(request.user)
        post.save()
        return Response(status=status.HTTP_200_OK)

    @action(detail=True)
    def unlike(self, request, pk=None):
        post = self.get_object()
        post.liked.remove(request.user)
        post.save()
        return Response(status=status.HTTP_200_OK)
