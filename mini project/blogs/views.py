from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import blog,form
# Create your views here.


def index(request):
    content=blog.objects.all()
    return render(request,'blogs/blog.html',{'content':content})

def page(request):
    
    return render(request,'blogs/page.html')


def detail(request,post_id):
    post = get_object_or_404(blog, id=post_id)
    return render(request,'blogs/detail.html',{'post':post})

def forms(request):
    if request.method=='POST':
        fname=request.POST.get('first_name')
        lname=request.POST.get('last_name')
        email=request.POST.get('email')
        phone=request.POST.get('contact-number')
        text=request.POST.get('message')
        value=form(first_name=fname,last_name=lname,email=email,phone=phone,text=text)
        print(value)
        value.save()
        print(value)
    return render(request,'blogs/form.html')

def about(request):
    return render(request,'blogs/about.html')



