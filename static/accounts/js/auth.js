/**
 * اسکریپت اعتبارسنجی فرم‌های احراز هویت
 */

document.addEventListener('DOMContentLoaded', function() {
    // اعتبارسنجی فرم ورود
    if (document.getElementById('loginForm')) {
        const loginForm = document.getElementById('loginForm');
        
        loginForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            let isValid = true;
            const email = document.getElementById('email');
            const password = document.getElementById('password');
            
            // اعتبارسنجی ایمیل
            if (email.value.trim() === '') {
                showError(email, 'لطفا نام کاربری یا ایمیل را وارد کنید');
                isValid = false;
            } else {
                showSuccess(email);
            }
            
            // اعتبارسنجی رمز عبور
            if (password.value.trim() === '') {
                showError(password, 'لطفا رمز عبور را وارد کنید');
                isValid = false;
            } else if (password.value.length < 6) {
                showError(password, 'رمز عبور باید حداقل 6 کاراکتر باشد');
                isValid = false;
            } else {
                showSuccess(password);
            }
            
            // اگر فرم معتبر بود، ارسال شود
            if (isValid) {
                // اینجا می‌توانید فرم را به سرور ارسال کنید
                alert('فرم با موفقیت ارسال شد!');
                // loginForm.submit();
            }
        });
    }
    
    // اعتبارسنجی فرم ثبت‌نام
    if (document.getElementById('registerForm')) {
        const registerForm = document.getElementById('registerForm');
        
        registerForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            let isValid = true;
            const name = document.getElementById('name');
            const username = document.getElementById('username');
            const email = document.getElementById('email');
            const password = document.getElementById('password');
            const confirmPassword = document.getElementById('confirm-password');
            const termsCheck = document.getElementById('termsCheck');
            
            // اعتبارسنجی نام کامل
            if (name.value.trim() === '') {
                showError(name, 'لطفا نام کامل را وارد کنید');
                isValid = false;
            } else {
                showSuccess(name);
            }
            
            // اعتبارسنجی نام کاربری
            if (username.value.trim() === '') {
                showError(username, 'لطفا نام کاربری را وارد کنید');
                isValid = false;
            } else if (username.value.length < 4) {
                showError(username, 'نام کاربری باید حداقل 4 کاراکتر باشد');
                isValid = false;
            } else {
                showSuccess(username);
            }
            
            // اعتبارسنجی ایمیل
            if (email.value.trim() === '') {
                showError(email, 'لطفا ایمیل را وارد کنید');
                isValid = false;
            } else if (!isValidEmail(email.value)) {
                showError(email, 'لطفا یک ایمیل معتبر وارد کنید');
                isValid = false;
            } else {
                showSuccess(email);
            }
            
            // اعتبارسنجی رمز عبور
            if (password.value.trim() === '') {
                showError(password, 'لطفا رمز عبور را وارد کنید');
                isValid = false;
            } else if (password.value.length < 6) {
                showError(password, 'رمز عبور باید حداقل 6 کاراکتر باشد');
                isValid = false;
            } else {
                showSuccess(password);
            }
            
            // اعتبارسنجی تکرار رمز عبور
            if (confirmPassword.value.trim() === '') {
                showError(confirmPassword, 'لطفا تکرار رمز عبور را وارد کنید');
                isValid = false;
            } else if (confirmPassword.value !== password.value) {
                showError(confirmPassword, 'رمز عبور و تکرار آن باید یکسان باشند');
                isValid = false;
            } else {
                showSuccess(confirmPassword);
            }
            
            // اعتبارسنجی قوانین و مقررات
            if (!termsCheck.checked) {
                showError(termsCheck, 'لطفا با قوانین و مقررات موافقت کنید');
                isValid = false;
            } else {
                showSuccess(termsCheck);
            }
            
            // اگر فرم معتبر بود، ارسال شود
            if (isValid) {
                // اینجا می‌توانید فرم را به سرور ارسال کنید
                alert('فرم ثبت‌نام با موفقیت ارسال شد!');
                // registerForm.submit();
            }
        });
    }
    
    // تابع نمایش خطا
    function showError(input, message) {
        const formGroup = input.parentElement;
        const errorElement = formGroup.querySelector('.error');
        
        if (!errorElement) {
            const errorElement = document.createElement('small');
            errorElement.className = 'error';
            errorElement.innerText = message;
            formGroup.appendChild(errorElement);
        } else {
            errorElement.innerText = message;
        }
        
        input.classList.add('is-invalid');
        input.classList.remove('is-valid');
    }
    
    // تابع نمایش موفقیت
    function showSuccess(input) {
        const formGroup = input.parentElement;
        const errorElement = formGroup.querySelector('.error');
        
        if (errorElement) {
            errorElement.remove();
        }
        
        input.classList.remove('is-invalid');
        input.classList.add('is-valid');
    }
    
    // تابع اعتبارسنجی ایمیل
    function isValidEmail(email) {
        const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(String(email).toLowerCase());
    }
});