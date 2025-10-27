from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import News, Blogs, Event, StudentClub, UserProfile

# ===============================================
# USER ADMIN (with Profile Inline)
# ===============================================

# Define an inline admin descriptor for UserProfile model
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserAdmin, self).get_inline_instances(request, obj)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# ===============================================
# BASE ADMIN (for shared News/Blogs logic)
# ===============================================

class BasePostAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_author_name', 'club', 'is_approved')
    list_filter = ('is_approved', 'club', 'author')
    list_editable = ('is_approved',)
    search_fields = ('title', 'content', 'author__username')
    ordering = ['-date']
    list_select_related = ('author', 'club') # Performance boost

    def get_author_name(self, obj):
        if obj.author:
            return f"{obj.author.first_name} {obj.author.last_name} (@{obj.author.username})"
        return "Anonymous"
    get_author_name.short_description = 'Author'

    # Automatically set author on creation in admin
    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user
        super().save_model(request, obj, form, change)

# ===============================================
# MODEL ADMINS
# ===============================================

@admin.register(News)
class NewsAdmin(BasePostAdmin):
    list_display = ('title', 'get_author_name', 'club', 'is_approved', 'date_start')
    ordering = ['-date_start']
    
    # Need to redefine 'date' for ordering to work
    def date(self, obj):
        return obj.date_start
    date.admin_order_field = 'date_start'


@admin.register(Blogs)
class BlogsAdmin(BasePostAdmin):
    list_display = ('title', 'get_author_name', 'club', 'is_approved', 'date')
    ordering = ['-date']
    
    # Need to redefine 'date' for ordering to work
    def date(self, obj):
        return obj.date
    date.admin_order_field = 'date'


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'event_date_end')
    ordering = ['-event_date']
    search_fields = ('title', 'content')

@admin.register(StudentClub)
class StudentClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_member_count')
    search_fields = ('name', 'members__username')
    filter_horizontal = ('members',) # Makes adding members much easier

    def get_member_count(self, obj):
        return obj.members.count()
    get_member_count.short_description = 'Member Count'

