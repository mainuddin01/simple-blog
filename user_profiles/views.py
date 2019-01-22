from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from .models import UserSocialLink
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

from blog.custom_mixins import SidebarDataMixin

from .forms import UserCreateForm, UserEditForm, UserSocialLinkForm


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
    success_url = reverse_lazy('home')
    template_name = 'user_profiles/user_update.html'

class UserListView(ListView):
    model = get_user_model()
    template_name = 'index.html'

class UserDetailView(SidebarDataMixin, DetailView):
    model = get_user_model()
    template_name = 'user_profiles/user_detail.html'


class UserSocialLinkCreateView(LoginRequiredMixin, CreateView):
    model = UserSocialLink
    fields = ('social_site', 'social_url')

    def form_valid(self, form):
        form.save(commit=False)
        form.instance.user = self.request.user
        return super().form_valid(form)


# def user_social_link_create_view(request, *args, **kwargs):
#     form = UserSocialLinkForm()
#     if request.method == 'POST':
#         form = UserSocialLinkForm(request.POST)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.user = request.user
#             instance.save()
#     if request.is_ajax():
#         return JsonResponse({'form': form})
#     return render(request, 'user_profiles/user_social_link_form.html', form)