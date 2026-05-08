from django.contrib.auth.models import User
from rest_framework import serializers
from posts.models import PostModel

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': True},
            'password': {
                'write_only': True,
                'required': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

class PostSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ['id', 'title', 'content', 'created', 'updated']

class UserProfileSerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'email', 'posts']

    def get_posts(self, obj):
        user_posts = PostModel.objects.filter(author=obj)
        return PostSimpleSerializer(user_posts, many=True).data
