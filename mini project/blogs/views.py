from django.shortcuts import render
from django.http import HttpResponse
from .models import blog
# Create your views here.


def index(request):
    content=blog.objects.all()
    return render(request,'blogs/blog.html',{'content':content})

def page(request):
    
    return render(request,'blogs/page.html')


def detail(request,post_name):
    return render(request,'blogs/detail.html')

def form(request):
    return render(request,'blogs/form.html')

def about(request):
    return render(request,'blogs/about.html')

