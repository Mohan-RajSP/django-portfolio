from django.contrib import admin
from django.urls import path, include

from .views import allBlogs,byBlogId

urlpatterns = [
   path("",allBlogs, name="allblogs"),
   path("<str:blogTitle>/",byBlogId, name='byBlogId')
]