from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Tag, Article, Comment, Like
from django.core.paginator import Paginator
from accounts.models import Profile
from django.contrib.auth.decorators import login_required

from django.contrib import messages


def get_pages_to_show(current_page, total_pages):
    """Utility function to determine which pagination pages to show."""
    if total_pages <= 3:
        return list(range(1, total_pages + 1))

    if current_page <= 2:
        return [1, 2, 3, '...', total_pages]

    if current_page >= total_pages - 1:
        return [1, '...', total_pages - 2, total_pages - 1, total_pages]

    return [1, '...', current_page - 1, current_page, current_page + 1, '...', total_pages]


def article_list(request):
    articles = Article.objects.filter(status=True)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 6)
    object_list = paginator.get_page(page_number)
    pages_to_show = get_pages_to_show(object_list.number, paginator.num_pages)

    context = {
        'articles': object_list,
        'pages_to_show': pages_to_show
    }
    return render(request, 'blog/article_list.html', context)


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    related_articles = Article.objects.filter(category__in=article.category.all(), status=True).exclude(id=article.id)[:2]

    user_has_liked = False
    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()
        if profile:
            user_has_liked = Like.objects.filter(article=article, user=profile).exists()

    viewed_articles = request.session.get('viewed_articles', [])
    if article.id not in viewed_articles:
        article.views += 1
        article.save(update_fields=['views'])
        viewed_articles.append(article.id)
        request.session['viewed_articles'] = viewed_articles

    if request.method == 'POST':
        body = request.POST.get('body')
        profile = get_object_or_404(Profile, user=request.user)
        Comment.objects.create(body=body, article=article, author=profile)
        return redirect('blog:article_detail', slug=slug)

    context = {
        'article': article,
        'related_articles': related_articles,
        'user_has_liked': user_has_liked,
    }
    return render(request, 'blog/article_detail.html', context)

@login_required
def like_article(request, slug):
    if not request.user.is_authenticated:
        messages.error(request, 'برای لایک کردن باید وارد شوید.')
        return redirect('blog:article_detail', slug=slug)

    article = get_object_or_404(Article, slug=slug)
    profile = get_object_or_404(Profile, user=request.user)
    like, created = Like.objects.get_or_create(article=article, user=profile)

    if not created:
        like.delete()

    return redirect('blog:article_detail', slug=slug)


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.author.user == request.user or request.user.is_staff:
        comment.delete()
    return redirect('blog:article_detail', slug=comment.article.slug)


def category_article(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = Article.objects.filter(status=True, category=category)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 6)
    object_list = paginator.get_page(page_number)
    pages_to_show = get_pages_to_show(object_list.number, paginator.num_pages)

    context = {
        'category': category,
        'articles': object_list,
        'pages_to_show': pages_to_show
    }
    return render(request, 'blog/category_article.html', context)


def tag_article(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    articles = Article.objects.filter(status=True, tags=tag)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 6)
    object_list = paginator.get_page(page_number)
    pages_to_show = get_pages_to_show(object_list.number, paginator.num_pages)

    context = {
        'tag': tag,
        'articles': object_list,
        'pages_to_show': pages_to_show
    }
    return render(request, 'blog/tag_article.html', context)


def author_detail(request, email):
    author = get_object_or_404(Profile, user__email=email)
    articles = Article.objects.filter(status=True, author=author).order_by('-created_at')
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 6)
    object_list = paginator.get_page(page_number)
    pages_to_show = get_pages_to_show(object_list.number, paginator.num_pages)

    context = {
        'author': author,
        'articles': object_list,
        'pages_to_show': pages_to_show,
    }
    return render(request, 'blog/author_detail.html', context)


def search(request):
    search_article = request.GET.get('search')
    articles = Article.objects.filter(title__icontains=search_article)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 6)
    object_list = paginator.get_page(page_number)
    pages_to_show = get_pages_to_show(object_list.number, paginator.num_pages)

    context = {
        'articles': object_list,
        'pages_to_show': pages_to_show,
    }
    return render(request, 'blog/article_list.html', context)


