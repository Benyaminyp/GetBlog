from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class UserDashboardView(LoginRequiredMixin , generic.TemplateView):
    template_name = "dashboard/index.html"
    
class ArticleCreateView(LoginRequiredMixin, generic.TemplateView):
    template_name = "dashboard/create-post.html" 

class UserProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = "dashboard/profile.html" 

class UserProfileUpdateView( LoginRequiredMixin, generic.TemplateView):
    template_name = "dashboard/edit-profile.html" 

class UserArticleListView(LoginRequiredMixin, generic.TemplateView):
    pass 

class ArticleUpdateView(LoginRequiredMixin, generic.TemplateView):
    pass 

class ArticleDeleteView(LoginRequiredMixin, generic.TemplateView):
    pass
