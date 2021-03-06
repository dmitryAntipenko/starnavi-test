from django.contrib.auth.models import User
from socnetapi.models import Post
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'password', 'email', 'posts')


class PostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=80)
    body = serializers.CharField(required=True, max_length=140)
    liked = serializers.HyperlinkedRelatedField(required=False, many=True, view_name='user-detail', queryset=User.objects.all())
    author = serializers.PrimaryKeyRelatedField(required=True, queryset=User.objects.all())

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'liked', 'author')
