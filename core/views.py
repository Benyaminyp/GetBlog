from django.shortcuts import render, redirect
from .forms import NewsletterForm
from .models import Contact


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


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, subject=subject, message=message)
        return redirect('core:home')
    return render(request, 'core/contact.html', {})
