from django.contrib import admin
from . import models
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin


@admin.register(models.SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['email', 'copy_right', 'instagram_link', 'telegram_link']


@admin.register(models.Newsletter)
class NewsletterAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['email', 'get_date_membership_jalali']

    @admin.display(description='تاریخ عضویت', ordering='date_membership')
    def get_date_membership_jalali(self, obj):
        return datetime2jalali(obj.date_membership).strftime('%a, %d %b %Y')


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_created_at_jalali', 'get_subject')
    list_filter = ('created_at',)
    search_fields = ('subject',)

    @admin.display(description='تاریخ ارسال', ordering='created_at')
    def get_created_at_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%a, %d %b %Y')

    class Media:
        js = ('main/js/custom_admin_1.js',)
