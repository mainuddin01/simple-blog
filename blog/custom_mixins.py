from .models import Post, Category, Tag

# this mixin sends sidebar data with context object
class SidebarDataMixin(object):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['popular_posts'] = Post.objects.all().order_by('-visited')[:4]
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        return context

        ## I want first 3 categorie which has more visits