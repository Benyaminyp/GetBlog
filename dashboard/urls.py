from . import views
from django.urls import path

app_name = "dashboard"

urlpatterns = [
    path("user/", views.UserDashboardView.as_view(), name="user_dashboard"),
    path("article/create/", views.ArticleCreateView.as_view(), name="create_article"),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path("profile/edit/", views.UserProfileUpdateView.as_view(), name="profile_edit"),
    path('article/edit/<str:slug>/', views.ArticleUpdateView.as_view(), name='article_edit'),
    path('article/delete/<str:slug>/', views.ArticleDeleteView.as_view(), name='article_delete'),
    
    
]
