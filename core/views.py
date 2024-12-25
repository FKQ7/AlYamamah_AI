from django.shortcuts import render
from .models import News
# Create your views here.
def index(request):
    return render(request, 'core/index.html')

#CRUD for news 
def news(request):
    news = News.objects.all().order_by('-date_start')
    return render(request, 'core/news.html', {'events': news})