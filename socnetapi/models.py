from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=80, blank=True, default='')
    body = models.TextField(max_length=140, default='')
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0, auto_created=True)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ('timestamp',)
