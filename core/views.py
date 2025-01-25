from django.shortcuts import render
from .models import News, Blogs, Event
import re
import bleach
def index(request):
    news = News.objects.all().order_by('-date_start')[:3]
    blogs = Blogs.objects.all().order_by('-date')[:2]
    events = Event.objects.all().order_by('event_date')
    for blog in blogs:
        blog.content = re.sub(r'<img[^>]*>', '', blog.content)
        blog.content = re.sub(r'<a[^>]*>|</a>', '', blog.content)
        blog.content = re.sub(r'<br[^>]*>|</br>', '', blog.content)
        blog.content = re.sub(r'<p>\s*&nbsp;\s*</p>', '', blog.content)
    # Clean up content for news
    for item in news:
        # Remove unwanted tags (e.g., <img>) if they exist
        item.content = re.sub(r'<img[^>]*>', '', item.content)
        item.content = re.sub(r'<a[^>]*>|</a>', '', item.content)
        item.content = re.sub(r'<br[^>]*>|</br>', '', item.content)
        item.content = re.sub(r'<p>\s*&nbsp;\s*</p>', '', item.content)


        # Sanitize content to ensure safe HTML
        item.content = bleach.clean(
            item.content,
            tags=['b', 'i', 'u', 'p', 'br', 'em'],  # Allow only these tags
            attributes={},  # Disallow all attributes
            strip=True  # Remove all disallowed tags completely
        )
    return render(request, 'core/index.html', {'news': news, 'blogs': blogs, 'events':events})

def news(request):
    news = News.objects.all().order_by('-date_start')
    for item in news:
        if item.content:
            # Remove unwanted tags (e.g., <img>)
            item.content = re.sub(r'<img[^>]*>', '', item.content)
            item.content = re.sub(r'<a[^>]*>|</a>', '', item.content)
            item.content = re.sub(r'<br[^>]*>|</br>', '', item.content)
            item.content = re.sub(r'<p>\s*&nbsp;\s*</p>', '', item.content)


            # Strip all HTML tags, retaining plain text only
            item.content = bleach.clean(
                item.content,
                tags=['b', 'i', 'u', 'p', 'br', 'em'],  # Allow only these tags
                attributes={},  # Disallow all attributes
                strip=True  # Remove all disallowed tags completely
            )
    return render(request, 'news/news.html', {'news': news})
from django.contrib.auth import authenticate
from django.contrib import auth


def blog(request):
    header_blogs = Blogs.objects.all().order_by('-date')[:4]
    all_blogs = Blogs.objects.all().order_by('-date')
    for blog in all_blogs:
        blog.content = re.sub(r'<img[^>]*>', '', blog.content)
        blog.content = re.sub(r'<a[^>]*>|</a>', '', blog.content)
        blog.content = re.sub(r'<p>\s*&nbsp;\s*</p>', '', blog.content)


    for blog in header_blogs:
        blog.content = re.sub(r'<img[^>]*>', '', blog.content)
        blog.content = re.sub(r'<a[^>]*>|</a>', '', blog.content)
        blog.content = re.sub(r'<p>\s*&nbsp;\s*</p>', '', blog.content)


    return render(request, 'blog/blog.html', {'header': header_blogs, 'blogs': all_blogs})

from django.shortcuts import get_object_or_404
def details_blog(request, id):
    header_blogs = Blogs.objects.all().order_by('-date')[:4]
    obj = get_object_or_404(Blogs, id=id)
    for blog in header_blogs:
        blog.content = re.sub(r'<img[^>]*>', '', blog.content)
    return render(request, 'blog/details.html', {'blog': obj,'header': header_blogs})

def details_news(request, id):
    obj = get_object_or_404(News, id=id)
    return render(request, 'news/details.html', {'news': obj})
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            messages.info(request, "اسم المستخدم أو كلمة المرور غير صحيحة. فضلاً تأكد من صحة المعلومات المدخلة.")
            return redirect('/login')

    return render(request, 'core/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BlogForm, NewsForm
class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blogs
    form_class  = BlogForm
    template_name = 'blog/create.html'
    success_url = '/'
    login_url = '/login/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class NewsCreateView(LoginRequiredMixin, CreateView):
    model = News
    form_class  = NewsForm
    template_name = 'news/create.html'
    success_url = '/'
    login_url = '/login/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)