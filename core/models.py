from django.db import models
from PIL import Image
import os
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    header_picture = models.ImageField(upload_to='header_pics/', null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


class StudentClub(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = RichTextUploadingField(blank=True, null=True)
    img = models.ImageField(
        _("Club Logo (Square)"),
        upload_to='club_logos/',
        help_text=_("A square logo for the club profile.")
    )
    header = models.ImageField(
        _("Club Header (Wide)"),
        upload_to='club_headers/',
        blank=True,
        null=True,
        help_text=_("An optional wide banner image for the club's detail page.")
    )
    members = models.ManyToManyField(User, blank=True, related_name='student_clubs')

    def __str__(self):
        return self.name

class News(models.Model):
    class Meta:
        ordering = ['-date_start']
        verbose_name_plural = "News"
        
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    img = models.ImageField(upload_to='news_images/')
    title = models.CharField(
        _("News Title"), max_length=250,
        null=False, blank=False
    )
    content = RichTextUploadingField()
    date_start = models.DateField(auto_created=True, auto_now=True)
    date_end = models.DateField(null=True, blank=True)
    tag_1 = models.CharField(max_length=100)
    tag_2 = models.CharField(max_length=100, null=True, blank=True)
    tag_3 = models.CharField(max_length=100, null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    
    club = models.ForeignKey(
        StudentClub, 
        on_delete=models.SET_NULL,  # Don't delete post if club is deleted
        null=True, 
        blank=True
    )

    def __str__(self):
        return self.title

class Blogs(models.Model):
    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Blogs"
        
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    img = models.ImageField(upload_to='blogs_images/')
    title = models.CharField(
        _("Blog Title"), max_length=250,
        null=False, blank=False
    )
    content = RichTextUploadingField()
    date = models.DateField(auto_now=True, auto_created=True)
    is_approved = models.BooleanField(default=False)

    # --- UPDATED FIELD ---
    club = models.ForeignKey(
        StudentClub, 
        on_delete=models.SET_NULL,  # Don't delete post if club is deleted
        null=True, 
        blank=True
    )

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    event_date = models.DateField()
    event_date_end = models.DateField()
    time_start = models.TimeField(null=True, blank=True)
    time_end = models.TimeField(null=True, blank=True)
    
    def __str__(self):
        return self.title

