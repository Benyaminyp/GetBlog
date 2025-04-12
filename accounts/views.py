from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignupForm
from .models import CustomUser
from django.shortcuts import redirect

class SignupView(generic.CreateView):
    '''
    'Handles user sign-up and logs the user in automatically after successful registration.
    '''
    model = CustomUser
    form_class = SignupForm
    template_name = 'registration/signup.html'
    success_url = "/"  # Redirect after signup
    
    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)  # Auto-login the user
        messages.success(self.request, "ثبت‌نام با موفقیت انجام شد و شما وارد شدید.")
        return response

