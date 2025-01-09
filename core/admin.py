from django.contrib import admin
from .models import News, Blogs, Event
# Register your models here.
admin.site.register(News)
admin.site.register(Blogs)
admin.site.register(Event)