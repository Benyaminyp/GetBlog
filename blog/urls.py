from django.urls import path, re_path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.article_list, name='article_list'),
    re_path(r'detail/(?P<slug>[-\w]+)/', views.article_detail, name='article_detail'),
    re_path(r'like/(?P<slug>[-\w]+)/', views.like_article, name='like'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    re_path(r'category/(?P<slug>[-\w]+)/', views.category_article, name='category_article'),
    re_path(r'tag/(?P<slug>[-\w]+)/', views.tag_article, name='tag_article'),
    path('author/<str:email>/', views.author_detail, name='author_detail'),
    path('search/', views.search, name='search_article'),
]
