from django.shortcuts import render
from .models import News, Blogs, Event
import re
# Create your views here.
def index(request):
    news = News.objects.all().order_by('-date_start')[:3]
    blogs = Blogs.objects.all().order_by('-date')[:2]
    events = Event.objects.all().order_by('-event_date')
    for blog in blogs:
        blog.content = re.sub(r'<img[^>]*>', '', blog.content)

    return render(request, 'core/index.html', {'news': news, 'blogs': blogs, 'events':events})

#CRUD for news 
def news(request):
    news = News.objects.all().order_by('-date_start')
    return render(request, 'core/news.html', {'news': news})


def blog(request):
    header_blogs = Blogs.objects.all().order_by('-date')[:4]
    all_blogs = Blogs.objects.all().order_by('-date')
    for blog in all_blogs:
        blog.content = re.sub(r'<img[^>]*>', '', blog.content)
    for blog in header_blogs:
        blog.content = re.sub(r'<img[^>]*>', '', blog.content)
    return render(request, 'blog/blog.html', {'header': header_blogs, 'blogs': all_blogs})

from django.shortcuts import get_object_or_404
def details(request, id):
    header_blogs = Blogs.objects.all().order_by('-date')[:4]
    obj = get_object_or_404(Blogs, id=id)
    for blog in header_blogs:
        blog.content = re.sub(r'<img[^>]*>', '', blog.content)
    return render(request, 'blog/details.html', {'blog': obj,'header': header_blogs})