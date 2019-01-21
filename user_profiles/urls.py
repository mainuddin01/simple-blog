from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'user_profiles'


urlpatterns = [
    path('', views.UserListView.as_view(), name='list'),
    path('login/', auth_views.LoginView.as_view(template_name='user_profiles/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.UserCreateView.as_view(), name='register'),
    path('<int:pk>/detail/', views.UserDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.UserUpdateView.as_view(), name='edit'),
]