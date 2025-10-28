import re
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.utils.html import strip_tags
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
import bleach

from .models import News, Blogs, Event, StudentClub, UserProfile
from .forms import BlogForm, NewsForm


# HELPER FUNCTIONS========================
def _get_plain_text_preview(html_content):
    """
    Strips all HTML tags from content to create a plain-text preview.
    Uses Django's built-in strip_tags for efficiency and safety.
    """
    if not html_content:
        return ""
    
    text = strip_tags(html_content)
    
    # Replace multiple spaces/nbsp with a single space
    text = re.sub(r'(&nbsp;|\s)+', ' ', text).strip()
    return text

# CORE & CLUB VIEWS
def index(request):
    news = News.objects.filter(is_approved=True).select_related('author', 'club').order_by('-date_start')[:3]
    blogs = Blogs.objects.filter(is_approved=True).select_related('author', 'club').order_by('-date')[:2]
    clubs = StudentClub.objects.all()
    
    today = timezone.now().date()
    events = Event.objects.filter(event_date_end__gte=today).order_by('event_date')

    for blog in blogs:
        blog.content_preview = _get_plain_text_preview(blog.content)
    for item in news:
        item.content_preview = _get_plain_text_preview(item.content)

    context = {
        'news': news,
        'blogs': blogs,
        'events': events,
        'clubs': clubs,
    }
    return render(request, 'core/index.html', context)

def clubs(request):
    all_clubs = StudentClub.objects.all().order_by('name')
    all_news = News.objects.filter(is_approved=True).select_related('author', 'club').order_by('-date_start')
    all_blogs = Blogs.objects.filter(is_approved=True).select_related('author', 'club').order_by('-date')
    
    for item in all_news:
        item.content_preview = _get_plain_text_preview(item.content)
    for blog in all_blogs:
        blog.content_preview = _get_plain_text_preview(blog.content)

    context = {
        'clubs': all_clubs,
        'all_news': all_news,
        'all_blogs': all_blogs,
    }
    return render(request, 'clubs/clubs.html', context)


def club_detail(request, club_id):
    club = get_object_or_404(StudentClub.objects.prefetch_related('members'), id=club_id)
    
    related_news = News.objects.filter(
        club=club, 
        is_approved=True
    ).select_related('author', 'club').order_by('-date_start')
    
    related_blogs = Blogs.objects.filter(
        club=club, 
        is_approved=True
    ).select_related('author', 'club').order_by('-date')

    for item in related_news:
        item.content_preview = _get_plain_text_preview(item.content)
    for blog in related_blogs:
        blog.content_preview = _get_plain_text_preview(blog.content)

    context = {
        'club': club,
        'related_news': related_news,
        'related_blogs': related_blogs,
    }
    return render(request, 'clubs/club_detail.html', context)


# WRITER PROFILE VIEW
def writer_profile(request, user_id):
    writer = get_object_or_404(User.objects.select_related('userprofile'), id=user_id)
    
    blogs = Blogs.objects.filter(
        author=writer, 
        is_approved=True
    ).select_related('club').order_by('-date')
    
    news = News.objects.filter(
        author=writer, 
        is_approved=True
    ).select_related('club').order_by('-date_start')

    writer_clubs = StudentClub.objects.filter(members=writer)

    for item in news:
        item.content_preview = _get_plain_text_preview(item.content)
    for blog in blogs:
        blog.content_preview = _get_plain_text_preview(blog.content)

    context = {
        'writer': writer,
        'blogs': blogs,
        'news': news,
        'writer_clubs': writer_clubs,
    }
    return render(request, 'writers/writer_details.html', context)


# BLOG & NEWS VIEWS
def news(request):
    all_news = News.objects.filter(is_approved=True).select_related('author', 'club').order_by('-date_start')
    for item in all_news:
        item.content_preview = _get_plain_text_preview(item.content)
        
    context = {
        'news': all_news
    }
    return render(request, 'news/news.html', context)

def blog(request):
    all_blogs = Blogs.objects.filter(is_approved=True).select_related('author', 'club').order_by('-date')
    
    header_blogs = all_blogs[:4]
    
    for blog in all_blogs:
        blog.content_preview = _get_plain_text_preview(blog.content)

    context = {
        'header': header_blogs,
        'blogs': all_blogs
    }
    return render(request, 'blog/blog.html', context)

def details_blog(request, id):
    blog_post = get_object_or_404(Blogs.objects.select_related('author', 'club'), id=id, is_approved=True)

    header_blogs = Blogs.objects.filter(is_approved=True).order_by('-date')[:4]
    for blog in header_blogs:
        blog.content_preview = _get_plain_text_preview(blog.content)

    context = {
        'blog': blog_post,
        'header': header_blogs
    }
    return render(request, 'blog/details.html', context)

def details_news(request, id):
    news_item = get_object_or_404(News.objects.select_related('author', 'club'), id=id, is_approved=True)
    context = {
        'news': news_item
    }
    return render(request, 'news/details.html', context)



# AUTHENTICATION & POST CREATION
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('index') 
        else:
            messages.info(request, "اسم المستخدم أو كلمة المرور غير صحيحة. فضلاً تأكد من صحة المعلومات المدخلة.")
            return render(request, 'core/login.html', {'email': email})

    return render(request, 'core/login.html')

def logout_view(request):
    auth.logout(request)
    return redirect('index')

class AuthorRequiredMixin(UserPassesTestMixin):
    """Ensures that the logged-in user is the author of the post."""
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class BlogCreateView(PermissionRequiredMixin, CreateView):
    model = Blogs
    form_class = BlogForm
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog')
    login_url = '/login/'
    permission_required = 'core.add_blogs' 
    raise_exception = True 

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Your blog post has been submitted for approval.")
        return super().form_valid(form)

class NewsCreateView(PermissionRequiredMixin, CreateView):
    model = News
    form_class = NewsForm
    template_name = 'news/news_form.html'
    success_url = reverse_lazy('news')
    login_url = '/login/'
    permission_required = 'core.add_news'
    raise_exception = True 

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Your news post has been submitted for approval.")
        return super().form_valid(form)


class BlogUpdateView(AuthorRequiredMixin, UpdateView):
    model = Blogs
    form_class = BlogForm
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog')
    login_url = '/login/'
    permission_required = 'core.change_blogs'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.is_approved = False
        messages.success(self.request, "Your post has been updated and sent for re-approval.")
        return super().form_valid(form)

class NewsUpdateView(AuthorRequiredMixin, UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'news/news_form.html'
    success_url = reverse_lazy('news')
    login_url = '/login/'
    permission_required = 'core.change_news'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.is_approved = False
        messages.success(self.request, "Your post has been updated and sent for re-approval.")
        return super().form_valid(form)


# --- New Delete Views ---

class BlogDeleteView(AuthorRequiredMixin, DeleteView):
    model = Blogs
    template_name = 'core/confirm_delete.html'
    success_url = reverse_lazy('blog')
    login_url = '/login/'
    permission_required = 'core.delete_blogs'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_title'] = self.object.title
        return context

class NewsDeleteView(AuthorRequiredMixin, DeleteView):
    model = News
    template_name = 'core/confirm_delete.html'
    success_url = reverse_lazy('news')
    login_url = '/login/'
    permission_required = 'core.delete_news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_title'] = self.object.title
        return context

