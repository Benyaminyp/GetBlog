from django.contrib import admin
from . import models
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin


@admin.register(models.Category)
class CategoryAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'get_created_at_jalali']
    prepopulated_fields = {'slug': ('title',)}

    @admin.display(description='تاریخ ایجاد', ordering='created_at')
    def get_created_at_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%a، %d %b %Y')


@admin.register(models.Tag)
class TagAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'get_created_at_jalali']
    prepopulated_fields = {'slug': ('title',)}

    @admin.display(description='تاریخ ایجاد', ordering='created_at')
    def get_created_at_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%a، %d %b %Y')


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['author', 'short_title', 'views', 'article_image', 'get_created_at_jalali', 'get_updated_at_jalali', 'status']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['status']
    list_filter = ['author', 'status']
    search_fields = ['title']

    def short_title(self, obj):
        if len(obj.title) > 20:
            return obj.title[:20] + '...'
        return obj.title
    short_title.short_description = 'عنوان مقاله'

    @admin.display(description='تاریخ ایجاد', ordering='created_at')
    def get_created_at_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%a، %d %b %Y')

    @admin.display(description='تاریخ به‌روزرسانی', ordering='updated_at')
    def get_updated_at_jalali(self, obj):
        return datetime2jalali(obj.updated_at).strftime('%a، %d %b %Y')


@admin.register(models.Comment)
class CommentAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['short_article_title', 'author', 'short_body', 'get_created_at_jalali', 'status']
    list_editable = ['status']

    def short_article_title(self, obj):
        if len(obj.article.title) > 10:
            return obj.article.title[:10] + '...'
        return obj.article
    short_article_title.short_description = 'مقاله مربوطه'

    def short_body(self, obj):
        if len(obj.body) > 20:
            return obj.body[:20] + '...'
        return obj.body
    short_body.short_description = 'متن نظر'

    @admin.display(description='تاریخ ایجاد', ordering='created_at')
    def get_created_at_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%a، %d %b %Y')


@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'short_article_title', 'get_created_at_jalali']

    def short_article_title(self, obj):
        if len(obj.article.title) > 10:
            return obj.article.title[:10] + '...'
        return obj.article
    short_article_title.short_description = 'مقاله مربوطه'

    @admin.display(description='تاریخ لایک', ordering='created_at')
    def get_created_at_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%a، %d %b %Y')