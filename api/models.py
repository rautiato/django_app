from django.db import models
from tastypie.resources import ModelResource
from blog.models import Post


class PostResource(ModelResource):
    class Meta:
        queryset = Post.objects.all()
        resource_name = 'posts'
        excludes = ['post_date']
