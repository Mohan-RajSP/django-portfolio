from django.shortcuts import render, get_object_or_404
from .models import Blog

def allBlogs(request):
    blogs = Blog.objects

    return render(request, "blogs/allblogs.html",{"blogs":blogs})

# Create your views here.

def byBlogId(request,blogTitle):
    blog = Blog.objects.get(title=blogTitle)
    print("blog",  blog)
    return render(request, "blogs/individual.html",{"blog":blog})
