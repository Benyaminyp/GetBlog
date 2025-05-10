from django.urls import include, path
from . import views


urlpatterns = [
    path("", include('django.contrib.auth.urls')),
    path("signup/", views.SignupView.as_view(), name="signup"),
        

]