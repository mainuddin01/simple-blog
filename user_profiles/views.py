from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

from .forms import UserCreateForm, UserEditForm


# Create your views here.
class UserCreateView(CreateView):
    model = get_user_model()
    # fields = ('username', 'password', 'first_name', 'last_name', 'email', 'profile_image')
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'user_profiles/user_register.html'

class UserUpdateView(UpdateView):
    model = get_user_model()
    # fields = ('first_name', 'last_name', 'email', 'profile_image')
    form_class = UserEditForm
    success_url = reverse_lazy('blog:home')
    template_name = 'user_profiles/user_update.html'

class UserListView(ListView):
    model = get_user_model()
    template_name = 'home'

class UserDetailView(DetailView):
    model = get_user_model()
    template_name = 'home'