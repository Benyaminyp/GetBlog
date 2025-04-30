from core.models import SiteSettings
from blog.models import Article, Tag, Category


def core_func(request):
    site_settings = SiteSettings.objects.first()

    return {
        'site_settings': site_settings,
    }


def blog_func(request):
    recent_articles = Article.objects.filter(status=True).order_by('-created_at')[:3]
    tags = Tag.objects.all()
    categories = Category.objects.all()
    return {
        'recent_articles': recent_articles,
        'tags': tags,
        'categories': categories,
    }
