from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse


def blog(request):
    context = {
    'posts' : Post.objects.all()
    }
    return render(request, 'blog/blog.html', context)

