from django.shortcuts import render
from posts.models import Post
from catagories.models import Category

def home(request,category_slug = None):
    data = Post.objects.all()
    if category_slug is not None:
        category = Category.objects.get(slug = category_slug)
        data = Post.objects.filter(category = category)
    catagories = Category.objects.all()
    return render(request,'home.html',{'data':data,'category':catagories})