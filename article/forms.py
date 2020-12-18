from django import forms
from .models import Article #şuanki klasörümüzdeki modelsten Article'ı dahil et demek.

# https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/ kodlar buradan
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title","content","article_image"]