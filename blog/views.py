from django.shortcuts import render
from django.views.generic import View, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q

from .forms import PostForm
from .models import Post, Category, Tag, Comment
from .custom_mixins import SidebarDataMixin

# Create your views here.
# class HomePageView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'blog/index.html', {})

class HomePageView(SidebarDataMixin, ListView):
    model = Post
    template_name = 'blog/index.html'
    queryset = model.objects.all()
    paginate_by = 4

class PostCreateView(CreateView):
    model = Post
    # fields = ('title', 'content', 'image', 'category', 'tags', 'publication_date')
    form_class = PostForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('home')

class PostDetailView(SidebarDataMixin, DetailView):
    model = Post

    def get(self, *args, **kwargs):
        self.object = self.get_object()
        self.object.post_visited()
        context = self.get_context_data(object=self.object)
        try:
            context['previous_post'] = Post.objects.filter(pk__lt=self.object.pk).order_by('-pk')[0]
        except:
            context['previous_post'] = Post.objects.last()
        context['recommended_post'] =  Post.objects.filter(author_id=self.object.author.id).all().order_by('?')[:3]
        return self.render_to_response(context)


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('home')

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    success_url = reverse_lazy('home')
    fields = ('name', 'description')

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    success_url = reverse_lazy('home')
    fields = ('name', 'description')

class CategoryDetailView(DetailView):
    model = Category

class TagCreateView(LoginRequiredMixin, CreateView):
    model = Tag
    success_url = reverse_lazy('home')
    fields = ('name',)

class TagUpdateView(LoginRequiredMixin, UpdateView):
    model = Tag
    success_url = reverse_lazy('home')
    fields = ('name',)

class TagDetailView(DetailView):
    model = Tag

