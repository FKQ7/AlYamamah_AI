from django import forms
from .models import Blogs, News, StudentClub

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        # List all fields you want in the form
        fields = [
            'title', 'img', 'content', 'club'
        ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get the user from the view
        super().__init__(*args, **kwargs)

        # If a user is passed, filter the 'club' queryset
        if user:
            self.fields['club'].queryset = StudentClub.objects.filter(members=user)
        
        # Make the field optional and add a "None" option
        self.fields['club'].required = False
        self.fields['club'].empty_label = "Individual Post (No Club)"


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # List all fields you want in the form
        fields = [
            'title', 'img', 'content', 'club', 
            'date_end', 'tag_1', 'tag_2', 'tag_3'
        ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get the user from the view
        super().__init__(*args, **kwargs)

        # If a user is passed, filter the 'club' queryset
        if user:
            self.fields['club'].queryset = StudentClub.objects.filter(members=user)
        
        # Make the field optional and add a "None" option
        self.fields['club'].required = False
        self.fields['club'].empty_label = "Individual Post (No Club)"
