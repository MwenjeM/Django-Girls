from django.shortcuts import render
from .models import Post  # Import Post model

def post_list(request):
    posts = Post.objects.all()  # Retrieve all posts from database
    return render(request, 'blog/post_list.html', {'posts': posts})
