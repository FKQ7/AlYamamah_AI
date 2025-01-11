from django.db import models
from PIL import Image
import os
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField

class News(models.Model):
    class Meta:
        ordering = ['-date_start']
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    img = models.ImageField(upload_to='news_images/')
    title = models.CharField(
        _("Blog Title"), max_length=250,
        null=False, blank=False
    )
    content = RichTextUploadingField()
    date_start = models.DateField(auto_created=True, auto_now=True)
    date_end = models.DateField(null=True, blank=True)
    tag_1 = models.CharField(max_length=100)
    tag_2 = models.CharField(max_length=100, null=True, blank=True)
    tag_3 = models.CharField(max_length=100, null=True, blank=True)
    

    def __str__(self):
        return self.title

class Blogs(models.Model):
    class Meta:
        ordering = ['-date']
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    img = models.ImageField(upload_to='blogs_images/')
    title = models.CharField(
        _("Blog Title"), max_length=250,
        null=False, blank=False
    )
    content = RichTextUploadingField()
    date = models.DateField(auto_now=True, auto_created=True)

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

