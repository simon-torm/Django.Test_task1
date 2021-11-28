from rest_framework import serializers
from ..models import Portfolio, Image, Comment
from django.contrib.auth.models import User


# User serializer for view in api response
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'image', 'name', 'body', 'created', 'active')


class ImageSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    portfolio = None
    class Meta:
        model = Image
        fields = ('id', 'portfolio', 'name', 'description', 'created', 'updated', 'comments')


class PortfolioSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Portfolio
        fields = ('id', 'name',  'description', 'author', 'created', 'updated', 'images')
