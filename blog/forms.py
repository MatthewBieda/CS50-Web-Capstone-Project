from django import forms
from .models import Article, Comments
from django.forms import ModelForm
from django import forms

#For adding styling to CreateView
class ArticleForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Article
        fields = ['title', 'body']

class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['contents']

        widgets = {
            'contents': forms.Textarea(attrs={'class': 'form-control'}),
        }

        labels = {
            'contents': 'Comment'
        }