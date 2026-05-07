from rest_framework import serializers
from posts.models import PostModel


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'author': {'read_only': True},
            'title': {},
            'content': {},
            'slug': {'read_only': True},
            'created': {'read_only': True},
            'updated': {'read_only': True},
        }