from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator , EmptyPage
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash
from django.template.loader import render_to_string
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import Profile
from blog.models import Article, Comment
from django.db.models import Sum
from .forms import (ArticleEditForm, 
                    ArticleCreateForm, 
                    ProfileForm , 
                    CustomUserChangeForm)
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
        user_articles = Article.objects.filter(author=profile).order_by("-updated_at","-created_at")
        
        total_articles = user_articles.count()
        
        total_views = user_articles.aggregate(Sum("views"))["views__sum"] or 0
        total_comments = Comment.objects.filter(author=profile).count()
        
        # paginate articles
        paginator = Paginator(user_articles, 5)
        page_obj = paginator.get_page(1)
        
        context["total_articles"] = total_articles
        context["total_views"] = total_views
        context["total_comments"] = total_comments
        context["user_articles"] = user_articles
        context["page_obj"] = page_obj
        return context
    
class LoadMoreArticlesView(LoginRequiredMixin, generic.View):
    """
    Loads more articles authored by the logged-in user via AJAX.
    Returns paginated article rows as HTML.
    Used for infinite scroll or "Load More" button.
    
    """
    def get(self, request, *args, **kwargs):
        page = request.GET.get("page", 1)
        profile = request.user.profile
        user_articles = Article.objects.filter(author=profile).order_by("-updated_at","-created_at")
        paginator = Paginator(user_articles, 5)
        page_obj = paginator.get_page(page)

        html = render_to_string("dashboard/partials/article_row.html", {
            "user_articles": page_obj.object_list
        }, request=request)

        return JsonResponse({
            "html": html,
            "has_next": page_obj.has_next()
        })     
        
class ArticleUpdateView(LoginRequiredMixin, generic.UpdateView):
    """
    Article Update View: This view allows the user to edit their published articles.
    - The user can only edit their own articles.
    - After a successful edit, a success message is displayed to the user confirming the update.
    """
    
    model = Article
    form_class = ArticleEditForm
    template_name = 'dashboard/edit-article.html'
    success_url = reverse_lazy('dashboard:user_dashboard')
    
    def get_queryset(self):
        return Article.objects.filter(author=self.request.user.profile)
    
    def form_valid(self, form):
        messages.success(self.request, "مقاله با موفقیت ویرایش شد.")
        return super().form_valid(form)

class ArticleDeleteView(LoginRequiredMixin, generic.View):
    """
    Article Delete View: This view allows the user to delete their published articles.
    - Only the author of the article or superusers are authorized to delete the article.
    - A success message is displayed to the user after successfully deleting the article.
    """
    
    def post(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        
        if article.author.user == request.user or request.user.is_superuser:
            article.delete()
            messages.success(request, "مقاله با موفقیت حذف شد.")
        else:
            messages.error(request, "شما اجازه حذف این مقاله را ندارید.")
        return redirect('dashboard:user_dashboard')
        
class ArticleCreateView(LoginRequiredMixin, generic.CreateView):
    """
    Article Create View: This view allows the user to create new articles.
    - After a successful creation, a success message is displayed confirming that the article was created.
    """
    
    template_name = "dashboard/create-post.html" 
    form_class = ArticleCreateForm
    success_url = reverse_lazy("dashboard:user_dashboard")
    
    def form_valid(self, form):
        form.instance.author = self.request.user.profile   
        messages.success(self.request, "مقاله با موفقیت ایجاد شد.") 
        return super().form_valid(form)
    
    

class UserProfileView(LoginRequiredMixin, generic.DetailView):
    """
    User Profile View: This view displays the profile information of the logged-in user.
    - The profile information is fetched from the `Profile` model associated with the user.
    """
    
    model = Profile
    template_name = "dashboard/profile.html" 
    context_object_name = "profile"
    
    def get_object(self):
        return Profile.objects.get(user=self.request.user)
    

class UserProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
    """
    User Profile Update View: This view allows the user to update their profile information.
    - The user can update their personal information, bio, and change their password.
    - If the user updates their password, the password will be validated, and the session will be updated to reflect the new password.
    """
    template_name = "dashboard/edit-profile.html" 
    model = Profile
    context_object_name = "profile"
    form_class = ProfileForm
    
    def get_object(self, queryset = None):
        return Profile.objects.get(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_form"] = CustomUserChangeForm(instance=self.request.user)
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        profile_form = self.get_form()
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        
        if profile_form.is_valid() and user_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            
            user = user_form.save(commit=False)
            password1 = user_form.cleaned_data.get("password1")
            if password1:
                user.set_password(password1)
            user.save()
            
            update_session_auth_hash(request, user)
            return redirect(reverse_lazy("dashboard:profile"))

        context = self.get_context_data()
        context['form'] = profile_form
        context['user_form'] = user_form
        return self.render_to_response(context)
    
    def form_valid(self, form):
        form.instance.author = self.request.user.profile   
        messages.success(self.request, "مقاله با موفقیت ویرایش شد.") 
        return super().form_valid(form)