from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from django import forms
from accounts.models import Profile
from blog.models import Article 
from ckeditor.widgets import CKEditorWidget
from django.core.exceptions import ValidationError

User = get_user_model()

class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["category","tags","title","slug","description", "image"]
        widgets = {
            "description":CKEditorWidget(),
        }
        

class ArticleEditForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category', 'tags', 'description', 'image']
        widgets = {
            "description":CKEditorWidget(),
        }

class CustomUserChangeForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, required=False, label="پسورد جدید", help_text="رمز عبور باید امن باشد.")
    password2 = forms.CharField(widget=forms.PasswordInput, required=False, label="تأیید پسورد جدید")
    
    class Meta:
        model = User
        fields = ['email']
    
    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if password1:
            try:
                validate_password(password1, self.instance)
            except ValidationError as e:
                raise forms.ValidationError(e.messages)
            return password1
                
                
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("پسوردها مطابقت ندارند.")
        return password2

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'bio', 'image']