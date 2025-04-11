from django.urls import include, path
from . import views

app_name = 'accounts'
urlpatterns = [
    path("", include('django.contrib.auth.urls')),
    path("signup/", views.SignupView.as_view(), name="signup")    

]