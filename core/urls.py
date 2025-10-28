from django.urls import path
from . import views

urlpatterns = [
    # --- Main Pages ---
    path('', views.index, name='index'),
    # ---  CLUB DETAIL URL ---
    path('clubs/', views.clubs, name='clubs'),
    path('clubs/<int:club_id>/', views.club_detail, name='club_detail'),

    # --- Writer Profile URL ---
    path('writer/<int:user_id>/', views.writer_profile, name='writer_profile'),

    # --- News URLs ---
    path('news/', views.news, name='news'),
    path('news/create/', views.NewsCreateView.as_view(), name='news-create'),
    path('news/<int:id>/', views.details_news, name='details_news'),
    path('news/<int:pk>/update/', views.NewsUpdateView.as_view(), name='news_update'), # New
    path('news/<int:pk>/delete/', views.NewsDeleteView.as_view(), name='news_delete'), # New

    # --- Blog URLs ---
    path('blog/', views.blog, name='blog'),
    path('blog/create/', views.BlogCreateView.as_view(), name='blog-create'),
    path('blog/<int:id>/', views.details_blog, name='details_blog'),
    path('blog/<int:pk>/update/', views.BlogUpdateView.as_view(), name='blog_update'), # New
    path('blog/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='blog_delete'), # New
    
    # --- Auth URLs ---
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
