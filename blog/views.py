from django.shortcuts import render
from .models import Post

def blog_views(request):
    all_posts = Post.objects.all()
    context = {
        'posts': all_posts
    }
    return render(request, 'blog/blog.html', context)

def blog_detail_views(request, id):
    post = Post.objects.get(pk=id)
    
    context = {
            "post": post,
        }
    
    return render(request, 'blog/blog_detail.html', context)