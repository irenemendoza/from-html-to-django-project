from django.shortcuts import render

from .models import Post

def blog_views(request):
    all_posts = Post.objects.all()
    context = {
        'post': all_posts
    }
    return render(request, 'blog/blog.html', context)

def blog_detail_views(request, id):
    all_posts = Post.objects.all()
    
    context = {
            "post": None,
        }
    

    for post in all_posts:
        if post.id == id:
              context["post"] = post

    return render(request, 'blog/blog_detail.html', context)