from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        errors = []
        if not (username and email and password and confirm_password):
            errors.append('همه فیلد ها باید پر شوند')
        if password != confirm_password:
            errors.append("رمز های عبور با هم تطابق ندارند")
        if User.objects.filter(username=username).exists():
            errors.append('نام کاربری در حای حاضر وجود دارد')

        if not errors:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            login(request, user)
            return redirect('home')

        for error in errors:
            messages.error(request, error)

    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        messages.error(request, 'نام کاربری یا رمز عبور نامعتبر')

    return render(request, 'login.html')



def logout_view(request):
    logout(request)
    messages.success(request, 'شما از اکانت خارج شدید!')
    return redirect('login')


def forgot_password_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        errors = []
        if not (email and new_password and confirm_password):
            errors.append("همه فیلد ها باید پر شوند")
        elif new_password != confirm_password:
            errors.append("رمز عبور ها با هم تطابق ندارند")
        else:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                errors.append("No account with this email exists")

        if not errors:
            user.set_password(new_password)
            user.save()

            messages.success(request, "رمز عبور تغییر یافت")
            return redirect('login')

        for error in errors:
            messages.error(request, error)

    return render(request, 'forgot_password.html')