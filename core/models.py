from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.html import format_html


class SiteSettings(models.Model):
    about_us_text = RichTextUploadingField(verbose_name='متن درباره ما')
    contact_us_text = models.TextField(verbose_name='متن تماس با ما')
    phone = models.CharField(max_length=14, null=True, blank=True, verbose_name='شماره تلفن')
    email = models.CharField(max_length=250, null=True, blank=True, verbose_name='ایمیل')
    copy_right = models.CharField(max_length=255, verbose_name='متن کپی رایت')
    instagram_link = models.CharField(max_length=250, null=True, blank=True, default='https://instagram.com/username', verbose_name='لینک اینستاگرام')
    telegram_link = models.CharField(max_length=250, null=True, blank=True, default='https://t.me/username', verbose_name='لینک تلگرام')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات سایت'

    def __str__(self):
        return self.email


class Newsletter(models.Model):
    email = models.EmailField(unique=True, verbose_name='ایمیل')
    date_membership = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ عضویت')

    class Meta:
        verbose_name = 'عضو خبرنامه'
        verbose_name_plural = 'اعضای خبرنامه'

    def __str__(self):
        return self.email


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')
    email = models.EmailField(verbose_name='ایمیل')
    subject = models.CharField(max_length=100,verbose_name='موضوع', null=True, blank=True)
    message = models.TextField(verbose_name='پیام')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ارسال')

    def get_subject(self):
        if self.subject:
            return self.subject
        else:
            return format_html("<span style='color: red;'>بدون موضوع</span>")

    get_subject.short_description = 'موضوع'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'پیام ها'
        verbose_name = 'پیام'
