from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Blogs, News

class BlogForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Blogs
        fields = ['title', 'content', 'img']

class NewsForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = News
        fields = ['title', 'content', 'img']