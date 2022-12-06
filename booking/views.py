from django.shortcuts import render
from .models import *


def index(request):
    desc = Desc.objects.all()
    banner = Banner.objects.all()
    comment = Comment.objects.all()
    link = Video.objects.all()
    blog = AboutUs.objects.all()
    content = {'banner':banner, 'desc':desc, 'comment':comment, 'link':link, 'blog':blog}
    return render(request, 'booking/index.html', content)

def about(request):
    blog = AboutUs.objects.all()
    images = AboutImg.objects.all()
    awards = Awards.objects.all()
    content = {'blog':blog, 'images':images, 'awards':awards}
    return render(request, 'booking/about-us.html', content)

def rooms(request):
    return render(request, 'booking/rooms.html')

def blog(request):
    blog = Blog.objects.all()
    content = {'blog':blog}
    return render(request, 'booking/blog.html', content)

def contact(request):
    contact = Contact.objects.all()
    content = {'contact': contact}
    return render(request, 'booking/contact.html', content)

def services(request):
    service = Service.objects.all()
    add_service = Add_service.objects.all()
    content = {'service':service, 'add_service':add_service}
    return render(request, 'booking/services.html', content)

