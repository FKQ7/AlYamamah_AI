from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('news', views.news),
    path('blog', views.blog),
    path('blog/<int:id>', views.details),
]