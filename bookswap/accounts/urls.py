from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register", views.RegisterUser.as_view(), name="signup"),
    path("login", auth_views.LoginView.as_view(redirect_field_name=""),  name="login"),
    path("logout", auth_views.LogoutView.as_view(next_page="signup"), name="logout")
]
