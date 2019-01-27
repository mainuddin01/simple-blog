from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q


from itertools import chain

from .forms import PostForm, CommentForm
from newsletter.forms import NewsUserForm
from .models import Post, Category, Tag, Comment
from .custom_mixins import SidebarDataMixin, get_sidebar_data

from user_profiles.models import UserProfile

# Create your views here.
# class HomePageView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'blog/index.html', {})

class HomePageView(SidebarDataMixin, ListView):
    model = Post
    template_name = 'blog/index.html'
    queryset = model.objects.all()
    paginate_by = 4

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = NewsUserForm()
        return context

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
        context['form'] = CommentForm()
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



class SearchView(View):

    def get(self, request, *args, **kwargs):
        query_string = request.GET.get('q', None)
        result = None
        if query_string:
            post_list = Post.objects.filter(
                Q(title__icontains=query_string) |
                Q(content__icontains=query_string) |
                Q(category__name__icontains=query_string) |
                Q(tags__name__icontains=query_string)
            ).all().distinct()
            category_list = Category.objects.filter(name__icontains=query_string).all().distinct()
            tag_list = Tag.objects.filter(name__icontains=query_string).all().distinct()
            author_list = UserProfile.objects.filter(
                Q(first_name__icontains=query_string) |
                Q(last_name__icontains=query_string) |
                Q(username__icontains=query_string) |
                Q(email__icontains=query_string)
            ).all().distinct()

            result = list(chain(post_list, category_list, tag_list, author_list))

            context = get_sidebar_data()
            context['query_string'] = query_string
            context['result'] = result

        return render(request, 'blog/search_results.html', context)


class CommentCreateView(View):

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            post_slug = kwargs.get('slug')
            print(post_slug)
            if post_slug:
                post = get_object_or_404(Post, slug=post_slug)
                instance.post = post
                if request.user.is_authenticated:
                    instance.name = request.user.username
                    instance.email = request.user.email
                instance.save()
            return HttpResponseRedirect(reverse('blog:detail', kwargs={'slug': post_slug}))
