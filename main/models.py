from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=200)
    category=models.ForeignKey(Category,related_name="posts",on_delete=models.CASCADE)
    description=models.TextField()

    def __str__(self):
        return self.title
