from django.db.models.functions import datetime

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404


from .models import Post


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'news/post_list.html'

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'news/post_list.html', {'posts': posts} )

def news_list(request):
    posts = Post.objects.all().order_by('-dataCreations')
    return render(request, 'news/list.html', {'posts': posts})

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'news/post_detail.html'

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'news/post_detail.html', {'posts': post})



