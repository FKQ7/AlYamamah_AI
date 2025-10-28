from django import forms
from .models import Blogs, News, StudentClub

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = [
            'title', 'img', 'content', 'club'
        ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['club'].queryset = StudentClub.objects.filter(members=user)
        
        self.fields['club'].required = False
        self.fields['club'].empty_label = "Individual Post (No Club)"


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            'title', 'img', 'content', 'club', 
            'date_end', 'tag_1', 'tag_2', 'tag_3'
        ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['club'].queryset = StudentClub.objects.filter(members=user)
        
        self.fields['club'].required = False
        self.fields['club'].empty_label = "Individual Post (No Club)"
