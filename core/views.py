from django.shortcuts import render, redirect
from .forms import NewsletterForm
from .models import Contact
from blog.models import Article
from django.db.models import Count


def home(request):
    published_articles = Article.objects.filter(status=True).order_by('-views')
    article = published_articles.first() if published_articles.exists() else None

    popular_articles = Article.objects.filter(status=True).order_by('-views')[:4]
    most_liked_articles = Article.objects.filter(status=True,like__isnull=False).annotate(like_count=Count('like')).order_by('-like_count')[:4]

    context = {
        'article': article,
        'popular_articles': popular_articles,
        'most_liked_articles': most_liked_articles,
    }
    return render(request, 'core/home.html', context)


def about(request):
    return render(request, 'core/about.html')


def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, subject=subject, message=message)
        return redirect('core:home')
    return render(request, 'core/contact.html', {})
