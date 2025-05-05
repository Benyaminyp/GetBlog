from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from blog.models import Article 

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = ['title', 'category', 'tags', 'description', 'image']