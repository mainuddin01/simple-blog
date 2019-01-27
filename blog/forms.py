from django import forms
from .models import Post, Comment

from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        widgets = {
            'content': SummernoteWidget(),
            # 'bar': SummernoteInplaceWidget()
        }

        fields = ('title', 'content', 'image', 'category', 'tags', 'publication_date')


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('message', 'name', 'email', 'website')