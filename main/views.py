from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import CategorySerializer,PostSerializer
from . models import Category,Post
# Create your views here.

class CategoryViewset(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class= CategorySerializer
    #permission_classes=(permissions.IsAuthenticatedOrReadOnly,)

class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    #permission_classes=(permissions.IsAuthenticatedOrReadOnly,)
