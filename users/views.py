from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser
from .forms import CustomUserCreationForm


class AccountView(generic.DetailView):
    model = CustomUser
    template_name = "users/account.html"
    context_object_name = "user"


class Register(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("signup")
    template_name = "register.html"
