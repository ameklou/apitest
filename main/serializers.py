from rest_framework import serializers
from .models import Category, Post


class CategorySerializer(serializers.ModelSerializer):
    #posts=serializers.PrimaryKeyRelatedField(many=True)
    class Meta:
        model=Category
        fields=('name','url')

class PostSerializer(serializers.ModelSerializer):
    category=serializers.StringRelatedField()
    class Meta:
        model=Post
        fields='__all__'
