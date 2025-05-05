from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Article, Comment
from django.db.models import Sum
from .forms import ArticleForm
# Create your views here.

class UserDashboardView(LoginRequiredMixin , generic.TemplateView):
    """ 
    Dashboard view for authenticated users displaying basic statistics:
    - Total number of published articles by the user
    - Total views across all their articles
    - Total number of comments on their articles
    """
    template_name = "dashboard/index.html"
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        profile = self.request.user.profile
        user_articles = Article.objects.filter(author=profile)
        
        total_articles = user_articles.count()
        
        total_views = user_articles.aggregate(Sum("views"))["views__sum"] or 0
        total_comments = Comment.objects.filter(article__author=profile).count()
        
        context["total_articles"] = total_articles
        context["total_views"] = total_views
        context["total_comments"] = total_comments
        context["user_articles"] = user_articles
        
        return context
        
class ArticleUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'dashboard/edit-article.html'
    success_url = reverse_lazy('dashboard:user_dashboard')
    
    def get_queryset(self):
        return Article.objects.filter(author=self.request.user.profile)

class ArticleDeleteView(LoginRequiredMixin, generic.View):
    def post(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        
        if article.author.user == request.user or request.user.is_superuser:
            article.delete()
            messages.success(request, "مقاله با موفقیت حذف شد.")
        else:
            messages.error(request, "شما اجازه حذف این مقاله را ندارید.")
        return redirect('dashboard:user_dashboard')
        
class ArticleCreateView(LoginRequiredMixin, generic.TemplateView):
    template_name = "dashboard/create-post.html" 

class UserProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = "dashboard/profile.html" 

class UserProfileUpdateView( LoginRequiredMixin, generic.TemplateView):
    template_name = "dashboard/edit-profile.html" 


