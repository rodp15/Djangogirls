from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
    posts = Post.object.all()
    return render(request, 'blog/post_list.html', {'posts':posts})
