from operator import truth

from tkinter.constants import CASCADE
from django.contrib.auth.models import User
from django.db import models

from django.db.models import Sum





class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        pr = sum(p.rating for p in Post.objects.filter(author=self)) * 3
        ur = sum(c.rating for c in Comment.objects.filter(user=self.user))
        cr = sum(c.rating for c in Comment.objects.filter(post_author=self))
        self.rating = pr + ur + cr
        self.save()

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Post(models.Model):
    news = "NW"
    articles = "AR"
    TYPE_CHOICES = ((news,"Новость") , (articles,"Статья"))
    author = models.ForeignKey(Author, on_delete=models.CASCADE,)
    post_type = models.CharField(max_length=100, choices=TYPE_CHOICES, default=news)
    category = models.ManyToManyField(Category, through="PostCategory")
    created_ad = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        if len(self.text) <= 124:
            return self.text
        else:
            return self.text[:124] + "..."

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)