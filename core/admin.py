from django.contrib import admin
from .models import News, Blogs, Event
# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_author_name', 'date_start')  # Customize the displayed fields
    ordering = ['-date_start']
    
    def get_author_name(self, obj):
        if obj.author:
            return f"{obj.author.first_name} {obj.author.last_name}"
        return "Anonymous"
    get_author_name.short_description = 'Author'

class BlogsAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_author_name', 'date')  # Use a custom method to display the author's full name
    ordering = ['-date']
    
    def get_author_name(self, obj):
        if obj.author:
            return f"{obj.author.first_name} {obj.author.last_name}"
        return "Anonymous"
    get_author_name.short_description = 'Author'

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'event_date_end')
    ordering = ['-event_date']

admin.site.register(News, NewsAdmin)
admin.site.register(Blogs, BlogsAdmin)
admin.site.register(Event, EventAdmin)