from django.db import models
from accounts.models import Profile
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.html import format_html
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(unique=True, max_length=50, verbose_name='عنوان دسته بندی')
    slug = models.SlugField(unique=True, max_length=50, allow_unicode=True, verbose_name='نامک')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(unique=True, max_length=50, verbose_name='عنوان برچسب')
    slug = models.SlugField(unique=True, max_length=50, allow_unicode=True, verbose_name='نامک')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'

    def __str__(self):
        return self.title


class Article(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='نویسنده مقاله')
    category = models.ManyToManyField(Category, related_name='articles', verbose_name='دسته بندی مربوطه')
    tags = models.ManyToManyField(Tag, blank=True, related_name='tags', verbose_name='برچسب مربوطه')
    title = models.CharField(unique=True, max_length=150, verbose_name='عنوان مقاله')
    slug = models.SlugField(unique=True, max_length=150, allow_unicode=True, verbose_name='نامک')
    description = RichTextUploadingField(verbose_name='محتوای مقاله')
    image = models.ImageField(upload_to='articles/', blank=True, null=True, verbose_name='بنر مقاله')
    status = models.BooleanField(default=False, verbose_name='منتشر شود؟')
    views = models.IntegerField(default=0, verbose_name='بازدید ها')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ به‌روزرسانی')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def article_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="80px" height="50px">')
        return format_html(f'<h3 style="color: red">تصویر ندارد</h3>')

    def get_absolute_url(self):
        return reverse('blog:article_detail', args=[self.slug])

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name='مقاله مربوطه')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments', verbose_name='نویسنده نظر')
    body = models.TextField(verbose_name='متن نظر')
    status = models.BooleanField(default=True, verbose_name='منتشر شود؟')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return self.article.title


class Like(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='likes', verbose_name='کاربر')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='مقاله مربوطه')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ لایک')

    def __str__(self):
        return self.article.title

    class Meta:
        verbose_name = 'لایک'
        verbose_name_plural = 'لایک ها'
