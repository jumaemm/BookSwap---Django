from django.shortcuts import render
from django.views.generic import (CreateView)
from .forms import CreateUserForm
from django.urls import reverse_lazy
# Create your views here.

class RegisterUser(CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"
