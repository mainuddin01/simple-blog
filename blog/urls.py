from django.urls import path

from . import views


app_name = 'blog'


urlpatterns = [
    # path('', views.HomePageView.as_view(), name='home'),
    path('post/create/', views.PostCreateView.as_view(), name='create'),
    path('post/<int:pk>/edit', views.PostEditView.as_view(), name='edit'),
    path('post/<int:pk>/detail', views.PostDetailView.as_view(), name='detail'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='delete'),
    path('categories/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('categories/<str:slug>/edit/', views.CategoryUpdateView.as_view(), name='category_edit'),
    path('categories/<str:slug>/detail/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('tags/create/', views.TagCreateView.as_view(), name='tag_create'),
    path('tags/<str:slug>/edit/', views.TagUpdateView.as_view(), name='tag_edit'),
    path('tags/<str:slug>/detail/', views.TagDetailView.as_view(), name='tag_detail'),
    path('search/', views.SearchView.as_view(), name='search'),
]