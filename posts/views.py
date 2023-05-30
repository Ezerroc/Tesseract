from django.views.generic import ListView, DetailView
from .models import Post

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

class PostListView(ListView):
    model = Post
    template_name = 'posts/blog.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
