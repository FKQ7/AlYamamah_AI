from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('news', views.news),
    path("login/", views.login, name='login'),
    path("logout/", views.logout, name='logout'),
    path('news/create', views.NewsCreateView.as_view(), name='news_create'),
    path('news/<int:id>', views.details_news),
    path('blog', views.blog),
    path('blog/create', views.BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:id>', views.details_blog),
    path('clubs', views.clubs, name='clubs'),
]