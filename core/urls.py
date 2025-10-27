from django.urls import path
from . import views

urlpatterns = [
    # --- Main Pages ---
    path('', views.index, name='index'),
    path('clubs/', views.clubs, name='clubs'),
    
    # --- NEW CLUB DETAIL URL ---
    path('clubs/<int:club_id>/', views.club_detail, name='club_detail'),

    path('writer/<int:user_id>/', views.writer_profile, name='writer_profile'),

    # --- News URLs ---
    path('news/', views.news, name='news'),
    path('news/<int:id>/', views.details_news, name='details_news'),
    path('news/create/', views.NewsCreateView.as_view(), name='news-create'),

    # --- Blog URLs ---
    path('blog/', views.blog, name='blog'),
    path('blog/<int:id>/', views.details_blog, name='details_blog'),
    path('blog/create/', views.BlogCreateView.as_view(), name='blog-create'),
    
    # --- Auth URLs ---
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
