from django.shortcuts import render, redirect
from .forms import NewsletterForm


def home(request):
    return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/about.html')


def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')



